# Library Management System (LMS)

This Python application is a simple yet functional Library Management System (LMS) that utilizes SQLite for database management. It allows users to manage members, authors, books, and borrowing records through a command-line interface.

## Features

- **Database Initialization**: Automatically creates the necessary database and tables if they do not exist.
    - create_tables( ): Sets up the database tables if they don't already exist.

<br>

- **Member Management**: Add new members with their names and ages.
    - add_members( ): Adds a new member to the database.

<br>

- **Author Management**: Add authors to the database.
    - add_authors( ): Inserts a new author into the database.

<br>

- **Book Management**: Register new books with details such as title, description, author, and publication year.
    - add_books( ): Records a new book in the database, linking it with an author.

<br>

- **Borrowing Records**: Track borrowing details for each book including borrower's information and borrow date.
    - add_borrow_record( ): Logs a borrowing event.

<br>

- **Book Issue Records**: Manage issues related to borrowed books, such as status, overdue records, notices, and fines.
    - record_book_issues( ): Tracks issues related to borrowed books, including status updates, overdue records, and fines.
<br>
<br>

## Database Schema
The system uses the following SQLite tables:

- **Members**: stores library member information.
- **Authors**: keeps author details.
- **Books Library**: contains books available in the library.
- **Borrow**: logs borrowing details.
- **Book** Issues: records issues related to book borrowings, including fines and overdue notifications.

![image](https://github.com/user-attachments/assets/533c7cc5-d78e-431b-ae51-f2f6739130f5)

<br>

## Sample Usage
1. Adds a new member to the database
```
After choosing option 1 from the main menu:
Enter the member's name: John Doe
Enter the member's age: 30
User John Doe added successfully
```
<br>

2. Register new books to the database
```
Enter the book title: Python Programming Fundamentals
Enter the publish year: 2021
Enter the book descriptions: A comprehensive guide to the basics of Python programming.
Enter the author's ID: 1
Python Programming Fundamentals added to the book library
```



## Improvements
- **Error Handling**: Implement comprehensive error handling around database operations.
<br>

- **Validation**: Ensure that all user inputs are validated before processing.
<br>

- **User Interface**: Upgrade to a graphical user interface for better interaction.
<br>

- **Function Modularization**: Refactor repetitive database connection code into a utility function.
<br>

- **Security Features**: Add security measures for data protection and privacy.
