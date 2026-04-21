import sqlite3
from lessons.database import create_table_students, insert_student, get_all_students, get_student_by_name, get_student_by_id, delete_student
from colorama import Fore, Back, Style

conn = sqlite3.connect('database.db')
# create_table_students(conn, "students")
# insert_student(conn, "Katya", 26, "Moscow")
print(get_all_students(conn))
one_student = get_student_by_name(conn, "Artem")
print(one_student)
two_students = get_student_by_id(conn, 2)
print(two_students)
print("delete student")
delete_student(conn, 2)
print(get_all_students(conn))
conn.close()

print(Fore.RED + "Hello colorama")
