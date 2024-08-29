import sqlite3
import tkinter as tk
from tkinter import messagebox


"""
Deletes the specified SQLite database file from the filesystem.

Args:
    db_file (str): The path to the database file to be deleted.

Raises:
    OSError: If the file cannot be deleted due to being in use, 
             lacking permissions, or not existing at the specified path.

Example:
    delete_database('LMS.db')  # Attempt to delete 'LMS.db'

Note:
    Use with caution as this operation is irreversible.
"""
# To use the delete_database function, uncomment the following line:

# import os
# def delete_database(db_file):
#     try:
#         os.remove(db_file)
#         print(f"Database '{db_file}' deleted successfully.")
#     except OSError as e:
#         print(f"Error: {e.strerror} - {e.filename}")
# delete_database('LMS.db')


# Function to create necessary tables in the database if they do not exist

def create_tables():
    conn = sqlite3.connect('LMS.db')
    cursor = conn.cursor()

    # Create table for members
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS members (
        members_library_card_id INTEGER PRIMARY KEY AUTOINCREMENT,
        members_name TEXT NOT NULL,
        members_age INTEGER NOT NULL)
    ''')

    # Create table for authors
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS authors(
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        author_name TEXT NOT NULL,
        author_age INTEGER NOT NULL)
    ''')

    # Create table for books in the library
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books_library(
        book_code INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        descriptions TEXT NOT NULL,
        author_id INTEGER,
        publish_year INTEGER NOT NULL,
        FOREIGN KEY (author_id) REFERENCES authors(author_id))
    ''')

    # Create table for borrow records
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS borrow(
        borrow_no INTEGER PRIMARY KEY AUTOINCREMENT,
        book_code INTEGER NOT NULL,
        borrow_date TEXT NOT NULL,
        members_library_card_id INTEGER NOT NULL,
        FOREIGN KEY (book_code) REFERENCES books_library(book_code),
        FOREIGN KEY (members_library_card_id) REFERENCES members(members_library_card_id))
    ''')

    # Create table for tracking book issues
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS book_issues (
        issue_number INTEGER PRIMARY KEY AUTOINCREMENT,
        book_issue_status TEXT NOT NULL,
        members_library_card_id INTEGER NOT NULL,
        overdue_records TEXT NOT NULL,
        overdue_notices BOOLEAN NOT NULL,
        total_fine_amount FLOAT NOT NULL,
        borrow_no INTEGER NOT NULL,
        FOREIGN KEY (borrow_no) REFERENCES borrow(borrow_no),
        FOREIGN KEY (members_library_card_id) REFERENCES members(members_library_card_id))
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Function to add a new member to the members table
def add_members(members_name, members_age):
    conn = sqlite3.connect('LMS.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO members (members_name, members_age) VALUES(?, ?)', (members_name, members_age))
    conn.commit()
    conn.close()
    print(f"User {members_name} added successfully")

# Function to add a new author to the authors table
def add_authors(author_name, author_age):
    conn = sqlite3.connect('LMS.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO authors (author_name, author_age) VALUES(? , ?)', (author_name, author_age))
    conn.commit()
    conn.close()
    print(f"Author {author_name} added successfully")

# Function to add a new book to the books library
def add_books(title, publish_year, descriptions, author_id):
    conn = sqlite3.connect('LMS.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books_library (title, publish_year, descriptions, author_id) VALUES (?, ?, ?, ?)', (title, publish_year, descriptions, author_id))
    conn.commit()
    conn.close()
    print(f"{title} added to the book library")

# Function to add a borrow record for a book
def add_borrow_record(book_code, borrow_date, members_library_card_id):
    conn = sqlite3.connect('LMS.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO borrow (book_code, borrow_date, members_library_card_id) VALUES(?, ?, ?)', (book_code, borrow_date, members_library_card_id))
    conn.commit()
    conn.close()
    print(f"Borrow record for book code {book_code} added")

# Function to record issues related to book borrowing
def record_book_issues(book_issue_status, members_library_card_id, overdue_records, overdue_notices, total_fine_amount, borrow_no):
    conn = sqlite3.connect('LMS.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO book_issues (book_issue_status, members_library_card_id, overdue_records, overdue_notices, total_fine_amount, borrow_no) VALUES(?, ?, ?, ?, ?, ?)', (book_issue_status, members_library_card_id, overdue_records, overdue_notices, total_fine_amount, borrow_no))
    conn.commit()
    conn.close()
    print(f"Book issue ({book_issue_status}) record added")

# Main function to drive the library management operations
# Main loop for user interaction
def main():
    create_tables()
    while True:
        print("1. Add Member")
        print("2. Add Authors")
        print("3. Add Book Library")
        print("4. Add Borrow Record")
        print("5. Add Book Issue Record")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            members_name = input("Enter the member's name: ")
            members_age = int(input("Enter the member's age: "))
            add_members(members_name, members_age)
        elif choice == "2":
            author_name = input("Enter the author's name: ")
            age = int(input("Enter the author's age: "))
            add_authors(author_name, age)
        elif choice == "3":
            book_title = input("Enter the book title: ")
            publish_year = int(input("Enter the publish year: "))
            book_descriptions = input("Enter the book descriptions: ")
            authors_id = int(input("Enter the author's ID: "))  # Request for author's ID
            add_books(book_title, publish_year, book_descriptions, authors_id)
        elif choice == "4":
            books_code = int(input("Enter the book code: "))
            borrow_date = input("Enter the borrow date (YYYY-MM-DD): ")
            members_library_card_id = int(input("Enter the member's library card ID: "))
            add_borrow_record(books_code, borrow_date, members_library_card_id)
        elif choice == "5":
            book_issue_status = input("Enter the book issue status: ")
            members_library_card_id = int(input("Enter the member's library card ID: "))
            overdue_records = input("Enter the overdue records(date): ")
            overdue_notices = input("True or False for overdue notices: ").lower() in ['true', '1', 't', 'y', 'yes']
            total_fine_amount = float(input("Enter the total fine amount: "))
            borrow_no = int(input("Enter the borrow number: "))
            record_book_issues(book_issue_status, members_library_card_id, overdue_records, overdue_notices, total_fine_amount, borrow_no)
        elif choice == "6":
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid option. Please input the correct number.")

if __name__ == "__main__":
    main()
