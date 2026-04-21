import sqlite3
from lessons.database import create_table_books, insert_books, get_all_books, delete_table

def get_books_by_author(connector,author):
    result = connector.execute("SELECT * FROM books WHERE author = ?",(author,))
    return result.fetchall()

def delete_book_by_id(connector,book_id):
    connector.execute("DELETE FROM books WHERE id = ?",(book_id,))
    connector.commit()

if __name__ == "__main__":
    conn = sqlite3.connect('../database.db')
    delete_table(conn, "books")
    create_table_books(conn, "books")
    insert_books(conn, "1984", "George Orwell", 1949, "Dystopian", 328, 5)
    insert_books(conn, "To Kill a Mockingbird", "Harper Lee", 1960, "Classic", 281, 4)
    insert_books(conn, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", 180, 6)
    insert_books(conn, "Moby Dick", "Herman Melville", 1851, "Adventure", 635, 2)
    insert_books(conn, "Pride and Prejudice", "Jane Austen", 1813, "Romance", 279, 3)
    insert_books(conn, "The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 7)
    insert_books(conn, "War and Peace", "Leo Tolstoy", 1869, "Historical", 1225, 1)
    insert_books(conn, "Crime and Punishment", "Fyodor Dostoevsky", 1866, "Psychological", 671, 2)
    insert_books(conn, "The Catcher in the Rye", "J.D. Salinger", 1951, "Classic", 214, 4)
    insert_books(conn, "Brave New World", "Aldous Huxley", 1932, "Science Fiction", 268, 5)
    print(get_all_books(conn))
    print(get_books_by_author(conn,"George Orwell"))
    delete_book_by_id(conn,1)
    print(get_all_books(conn))
    conn.close()
