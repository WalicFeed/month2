import sqlite3

def create_table_students(conn, table_name):
    conn.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    city TEXT NOT NULL)
    ''')

def delete_table(conn, table_name):
    conn.execute(f'''
    DROP TABLE IF EXISTS {table_name}
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
    return result.fetchall()

def get_student_by_name(conn, name):
    result = conn.execute('SELECT * FROM students WHERE name = ?', (name,))
    return result.fetchone()

def get_student_by_id(conn, student_id):
    result = conn.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    return result.fetchone()

def delete_student(conn, student_id):
    conn.execute(f'''
    DELETE FROM students WHERE id = ?''', (student_id,))
    conn.commit()

def change_student(conn, student_id, name, age, city):
    conn.execute(f'''
    UPDATE students SET name = ?, age = ?, city = ? WHERE id = ?''', (name, age, city, student_id))
    conn.commit()

def create_table_books(conn, table_name):
    conn.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    author TEXT NOT NULL,
    publication_year INTEGER NOT NULL,
    genre TEXT NOT NULL,
    number_of_pages INTEGER NOT NULL,
    number_of_copies INTEGER NOT NULL)''')

def insert_books(conn, name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute(
    "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES (?, ?, ?, ?, ?, ?)",
    (name, author, publication_year, genre, number_of_pages, number_of_copies))
    conn.commit()

def get_all_books(conn):
    result = conn.execute('SELECT * FROM books')
    return result.fetchall()

