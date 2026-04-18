import sqlite3

def create_table_students(conn, table_name):
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
    conn.commit()
    return result.fetchall()

def create_table_books(conn, table_name):
    conn.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
    name TEXT NOT NULL,
    author TEXT NOT NULL,
    publication_year INTEGER NOT NULL,
    genre TEXT NOT NULL,
    number_of_pages INTEGER NOT NULL,
    number_of_copies INTEGER NOT NULL)''')
    conn.commit()

def insert_books(conn, name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute(
    "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES (?, ?, ?, ?, ?, ?)",
    (name, author, publication_year, genre, number_of_pages, number_of_copies))
    conn.commit()

def get_all_books(conn):
    result = conn.execute('SELECT * FROM books')
    conn.commit()
    return result.fetchall()

