
from book import Book
import sql_sdk as sdk


def print_menu():
    print("""
    1. Print all books
    2. Add a book
    3. Update a book
    4. Delete a book
    """)

while True:
    print_menu()
    response = int(input())
    if response == 1:
        print("Printing all books")
        for book in sdk.get_books():
            print(book)
    elif response == 2:
        print("What is the name of the book?")
        title = input()
        print('How many pages is the books?')
        pages = int(input())
        book = Book(title, pages)
        sdk.add_book(book)
    elif response == 3:
        print("What is the current title?")
        title = input()
        print('Current number of pages?')
        pages = input()

        book = Book(title, pages)

        print('What is the new title?')
        new_title = input()
        print('New number of pages?')
        new_pages = input()

        print(sdk.update_book(book, new_title, new_pages))

    elif response == 4:
        print("What is the title?")
        title = input()
        print('Number of pages?')
        pages = input()

        book = Book(title, pages)
        print(sdk.delete_book(book))
    else:
        print("Thanks for using the app")
        break