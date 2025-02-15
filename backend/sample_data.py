from neon_connect import create_connection_pool

def insert_sample_data():
    connection_pool = create_connection_pool()
    conn = connection_pool.getconn()
    cur = conn.cursor()

    teachers = [("Amy",), ("Betty",)]

    students = [
        # (name, teacher_id)
        ("Andy", 1),
        ("Bryan", 1),
        ("Charm", 2),
        ("Danielle", 2),
        ("Elliot", 1),
        ("Fredrick", 1),
        ("Godfry", 2),
        ("Hildy", 2),
        ("Indigo", 1),
        ("Jessica", 2)
    ]

    grades = [
        # (student_id, semester, grade)
        (1, 1, 4.0),
        (1, 2, 3.5),
        (1, 3, 4.5),
        (1, 4, 3.9),
        (1, 5, 3.8),
        (1, 6, 3.5),
        (1, 7, 3.0),
        (1, 8, 2.5),

        (2, 1, 1.0),
        (2, 2, 1.5),
        (2, 3, 2.5),
        (2, 4, 2.9),
        (2, 5, 3.8),
        (2, 6, 3.5),
        (2, 7, 4.0),
        (2, 8, 4.5),

        (3, 1, 1.0),
        (3, 2, 3.5),
        (3, 3, 4.5),
        (3, 4, 2.9),
        (3, 5, 3.3),
        (3, 6, 3.4),
        (3, 7, 5.0),
        (3, 8, 2.5),

        (4, 1, 4.0),
        (4, 2, 3.5),
        (4, 3, 4.5),
        (4, 4, 3.9),
        (4, 5, 3.8),
        (4, 6, 3.5),
        (4, 7, 3.0),
        (4, 8, 2.5),

        (5, 1, 1.0),
        (5, 2, 1.5),
        (5, 3, 2.5),
        (5, 4, 2.9),
        (5, 5, 3.8),
        (5, 6, 3.5),
        (5, 7, 4.0),
        (5, 8, 4.5),

        (6, 1, 1.0),
        (6, 2, 3.5),
        (6, 3, 4.5),
        (6, 4, 2.9),
        (6, 5, 3.3),
        (6, 6, 3.4),
        (6, 7, 5.0),
        (6, 8, 2.5),

        (7, 1, 4.0),
        (7, 2, 3.5),
        (7, 3, 4.5),
        (7, 4, 3.9),
        (7, 5, 3.8),
        (7, 6, 3.5),
        (7, 7, 3.0),
        (7, 8, 2.5),

        (8, 1, 1.0),
        (8, 2, 1.5),
        (8, 3, 2.5),
        (8, 4, 2.9),
        (8, 5, 3.8),
        (8, 6, 3.5),
        (8, 7, 4.0),
        (8, 8, 4.5),

        (9, 1, 1.0),
        (9, 2, 3.5),
        (9, 3, 4.5),
        (9, 4, 2.9),
        (9, 5, 3.3),
        (9, 6, 3.4),
        (9, 7, 5.0),
        (9, 8, 2.5),

        (10, 1, 4.0),
        (10, 2, 3.5),
        (10, 3, 4.5),
        (10, 4, 3.9),
        (10, 5, 3.8),
        (10, 6, 3.5),
        (10, 7, 3.0),
        (10, 8, 2.5),

    ]

    try:
        cur.executemany("INSERT INTO teachers (name) VALUES (%s)", teachers)

        cur.executemany(
            "INSERT INTO students (name, teacher_id) VALUES (%s, %s)", students
        )

        cur.executemany(
            "INSERT INTO grades (student_id, semester, grade) VALUES (%s, %s, %s)",
            grades,
        )

        conn.commit()
        print("Sample data inserted successfully.")
    except Exception as e:
        print(f"Error inserting sample data: {e}")
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    insert_sample_data()
