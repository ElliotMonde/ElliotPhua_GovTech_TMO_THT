def get_teacher(cur, teacher_id: int):
    if teacher_id is None:
        return {"error" : "No teacher id provided."}
    sql_str = """
    SELECT name FROM teachers WHERE id = %s
    """
    cur.execute(sql_str, (teacher_id,))
    res = cur.fetchall()
    return res
