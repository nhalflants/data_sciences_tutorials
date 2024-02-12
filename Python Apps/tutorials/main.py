from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """

def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print('Unknown command')
        user_input = input(USER_CHOICE)

def prompt_add_book():
    book_title = input('Enter book title: ')
    book_author = input('Enter book author: ')
    database.add_book(book_title, book_author)
    
def list_books():
    books = database.get_books()
    for book in books:
        read = 'Yes' if book['read'] else 'No'
        print(f"Book title: {book['name']} by author: {book['author']}, read: {read}")

def prompt_read_book():
    name = input('Enter the name of the book you read: ')
    database.mark_book_as_read(name)

def prompt_delete_book():
    remove_book_title = input("Book title to delete: ")
    database.delete_book(remove_book_title)

if __name__ == '__main__':
    menu()