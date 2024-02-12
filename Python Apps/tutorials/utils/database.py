from typing import List, Dict, Union
from .database_connection import DatabaseConnection
"""
Concerned with storing and retrieving books from csv file
Format of the csv file:
name,author,read\n
"""
books_file = 'books.txt'

Book = Dict(str, Union(str, int))

def create_book_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

def add_book(name: str, author: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO books VALUES("{name}", "{author}", 0)')

def get_books() -> List[Book]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    return books
    # with open(books_file, 'r') as file:
    #     lines = [line.strip().split(',') for line in file.readline()]
    # return [{'name': line[0], 'author': line[1], 'read': line[2]} for line in lines]
    

def mark_book_as_read(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))

    # books = get_books()
    # for book in books:
    #     if book['name'] == name:
    #         book['read'] = '1'
    # _save_all_books(books)
    
def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}")

def delete_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (name,))

    # books = get_books()
    # books = [book for book in books if book['name'] != name]
    # _save_all_books(books)