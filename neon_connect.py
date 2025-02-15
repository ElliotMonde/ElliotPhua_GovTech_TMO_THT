import os
from psycopg2 import pool
from dotenv import load_dotenv

def create_connection_pool() -> pool.SimpleConnectionPool | None:
    load_dotenv()
    connection_string = os.getenv("DATABASE_URL")
    try:
        connection_pool = pool.SimpleConnectionPool(
            1,
            10,
            connection_string,
        )
        if connection_pool:
            print("Connection pool created successfully")
        return connection_pool
    except Exception as e:
        print(f"Error creating connection pool: {e}")
