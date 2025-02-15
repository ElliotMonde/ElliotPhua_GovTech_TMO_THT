import os
import atexit
from typing import Any, Literal, LiteralString
from flask import Flask, jsonify, request
from init_tables import init_tables
from neon_connect import create_connection_pool
from students_services import *

app = Flask(__name__)

# Initialize connection pool and connect with neon db
connection_pool = create_connection_pool()

if connection_pool is None:
    raise Exception("Database connection pool was not created successfully")

init_tables(connection_pool)


@app.before_request
def before_request() -> None:
    if connection_pool is None:
        raise Exception("Database connection pool was closed.")


@app.route("/")
def homepage() -> LiteralString:
    return "Hello, Welcome to the GPA Monitoring Tool!\nMade with love by Elliot Phua"


@app.route("/students", methods=["GET"])
def get_all_students() -> tuple[Any, Literal[200]] | tuple[Any, Literal[400]]:
    conn = None
    try:
        conn = connection_pool.getconn()
        cur = conn.cursor()
        res = get_students(cur)
        return jsonify(res), 200
    except Exception as e:
        print(f"Database error: {e}")
        return jsonify({"error": "Unable to fetch student details."}), 400
    finally:
        if conn:
            connection_pool.putconn(conn)


@app.route("/student/<int:student_id>", methods=["PATCH"])
def update_teacher_of_student(student_id: int):
    new_teacher_id = request.json.get("new_teacher_id")
    if not new_teacher_id:
        return jsonify({"error": "No teacher id provided."}), 400
    conn = None
    try:
        conn = connection_pool.getconn()
        cur = conn.cursor()
        res = update_student(conn, cur, student_id=student_id, teacher_id=new_teacher_id)
        if res:
            return jsonify({"message": "Successfully updated student's teacher."}), 200
        else:
            return jsonify({"error": "Failed to update student's teacher. Either student not found or no change was made"}), 400
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Unable to update student's teacher."}), 500
    finally:
        if conn:
            connection_pool.putconn(conn)


@app.route("/students-grades", methods=["GET"])
def get_all_student_grades() -> tuple[Any, Literal[200]] | tuple[Any, Literal[400]]:
    earliest_semester = request.args.get("earliest_semester")
    latest_semester = request.args.get("latest_semester")
    try:
        conn = connection_pool.getconn()
        cur = conn.cursor()
        res = get_students(cur, earliest_semester=earliest_semester, latest_semester=latest_semester)
        return jsonify(res), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Unable to retrieve students' grades."}), 500
    finally:
        if conn:
            connection_pool.putconn(conn)

def on_app_close() -> None:
    global connection_pool
    if connection_pool:
        print("Closing connection pool...")
        connection_pool.closeall()
        connection_pool = None


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

atexit.register(on_app_close)
