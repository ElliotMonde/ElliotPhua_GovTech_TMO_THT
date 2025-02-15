from teachers_service import get_teacher


def get_students(cur, earliest_semester : int | None, latest_semester : int | None) -> list[dict[str, str | int]] | dict[str, str]:
    if earliest_semester is None:
        earliest_semester = 1
    else: 
        earliest_semester = int(earliest_semester)
    if latest_semester is None:
        latest_semester = 8
    else:
        latest_semester = int(latest_semester)

    if latest_semester > 8 or latest_semester < 1 or earliest_semester < 1 or earliest_semester > 8:
        return {"error" : "Earliest and latest semester must have a value between 1 and 8 inclusive."}
    if latest_semester < earliest_semester:
        return {"error": "Earliest semester must have a lower value than latest semester."}
    
    sql_str = """
            SELECT 
                students.id as student_id,
                students.name as student,
                teachers.name as teacher,
                ROUND(COALESCE(AVG(grades.grade), 0), 2) as cumulative_grade
            FROM students
            LEFT JOIN teachers ON students.teacher_id = teachers.id
            LEFT JOIN grades ON students.id = grades.student_id
            WHERE grades.semester >= %s AND grades.semester <= %s
            GROUP BY students.id, teachers.name;
        """
    cur.execute(sql_str, (earliest_semester, latest_semester))
    students = cur.fetchall()
    formatted_students_response = sorted(
        [
            {
                "student_id": student[0],
                "student_name": student[1],
                "teacher_name": student[2],
                "cumulative_GPA": float(student[3]),
            }
            for student in students
        ],
        key=lambda x: x["student_id"],
    )
    return formatted_students_response


def update_student(
    conn,
    cur,
    student_id: int,
    teacher_id: int | None = None,
    student_name: str | None = None,
) -> bool:
    if (teacher_id is None and student_name is None) or student_id is None:
        return False

    fields = []
    values = []

    if teacher_id is not None:
        if get_teacher(cur, teacher_id):
            fields.append("""teacher_id = %s""")
            values.append(teacher_id)
        else:
            return False

    if student_name is not None:
        fields.append("""name = %s""")
        values.append(student_name)

    values.append(student_id)

    try:
        sql_str = f"""
        UPDATE students 
        SET {', '.join(fields)}
        WHERE id = %s;
        """
        cur.execute(sql_str, tuple(values))
        conn.commit()
        return cur.rowcount == 1
    except Exception as e:
        print(f"Error while updating student: {e}")
        return False
