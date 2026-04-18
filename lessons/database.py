import sqlite3

def create_table(conn, table_name):
    conn.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    city TEXT NOT NULL)
    ''')
    conn.commit()

def delete_table(conn, table_name):
    conn.execute(f'''
    DROP TABLE {table_name}
    ''')
    conn.commit()

def insert_student(conn, name, age: int, city):
    conn.execute(
        "INSERT INTO students (name, age, city) VALUES (?, ?, ?)",
        (name, age, city)
    )
    conn.commit()

def get_all_students(conn):
    result = conn.execute('SELECT * FROM students')
    conn.commit()
    return result.fetchall()