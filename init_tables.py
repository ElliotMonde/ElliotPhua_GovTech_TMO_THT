def init_tables(connection_pool):
    conn = connection_pool.getconn()
    cur = conn.cursor()

    # SQL to initialise tables if not exists
    create_teachers_table = """
    CREATE TABLE IF NOT EXISTS teachers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
    );
    """

    create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    teacher_id INT REFERENCES teachers(id) ON DELETE SET NULL
    );
    """

    create_grades_table = """
    CREATE TABLE IF NOT EXISTS grades (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id) ON DELETE CASCADE,
    semester INT NOT NULL,
    grade NUMERIC(2,1) NOT NULL CHECK (grade >= 0.0 AND grade <= 5.0)
    );    
    """

    try:
        cur.execute(create_teachers_table)
        cur.execute(create_students_table)
        cur.execute(create_grades_table)
        conn.commit()
        print("Tables created successfully.")
    except:
        print("Unable to initialise tables.")

    cur.close()
    connection_pool.putconn(conn)
