def get_teacher(cur, teacher_id: int):
    if teacher_id is None:
        return {"error" : "No teacher id provided."}
    sql_str = """
    SELECT name FROM teachers WHERE id = %s
    """
    cur.execute(sql_str, (teacher_id,))
    res = cur.fetchall()
    return res

def get_teachers(cur):
    sql_str = """
    SELECT id, name
    FROM teachers;
    """

    cur.execute(sql_str)
    res = cur.fetchall()
    formatted_response = sorted(
        [
            {
                "id": teacher[0],
                "name": teacher[1],
            }
            for teacher in res
        ],
        key=lambda x: x["id"],
    )
    return formatted_response
