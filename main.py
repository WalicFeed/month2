import sqlite3
from lessons.database import create_table, insert_student, get_all_students

conn = sqlite3.connect('database.db')
# create_table(conn, "students")
# insert_student(conn, "Katya", 26, "Moscow")
print(get_all_students(conn))
conn.close()

