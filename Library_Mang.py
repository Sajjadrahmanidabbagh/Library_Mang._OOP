#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:10:11 2024
@author: sajjad
"""

class Book:
    def __init__(self, book_id, name, quantity):
        self.book_id = book_id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.book_id}, Name: {self.name}, Quantity: {self.quantity}"

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []  # List to track borrowed books

    def __str__(self):
        return f"ID: {self.user_id}, Name: {self.name}, Borrowed Books: {[book.name for book in self.borrowed_books]}"

class Admin:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, book_id, name, quantity):
        if book_id in self.books:
            print("Book with this ID already exists.")
        else:
            self.books[book_id] = Book(book_id, name, quantity)
            print("Book is added successfully!")

    def print_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books.values():
                print(book)

    def print_books_by_prefix(self, prefix):
        found = False
        for book in self.books.values():
            if book.name.lower().startswith(prefix.lower()):
                print(book)
                found = True
        if not found:
            print("No books found with the given prefix.")

    def add_user(self, user_id, name):
        if user_id in self.users:
            print("User with this ID already exists.")
        else:
            self.users[user_id] = User(user_id, name)
            print("User is added successfully!")

    def borrow_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User does not exist.")
        elif book_id not in self.books:
            print("Book does not exist.")
        elif self.books[book_id].quantity <= 0:
            print("Book is not available.")
        else:
            book = self.books[book_id]
            user = self.users[user_id]
            book.quantity -= 1
            user.borrowed_books.append(book)
            print("Book borrowed successfully!")

    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User does not exist.")
        else:
            user = self.users[user_id]
            for book in user.borrowed_books:
                if book.book_id == book_id:
                    user.borrowed_books.remove(book)
                    self.books[book_id].quantity += 1
                    print("Book returned successfully!")
                    return
            print("The user did not borrow this book.")

    def print_users_borrowed_books(self, user_id):
        if user_id not in self.users:
            print("User does not exist.")
        else:
            user = self.users[user_id]
            if not user.borrowed_books:
                print("User has not borrowed any books.")
            else:
                for book in user.borrowed_books:
                    print(book)

    def print_users(self):
        if not self.users:
            print("No users in the system.")
        else:
            for user in self.users.values():
                print(user)


def main():
    admin = Admin()

    while True:
        print("\nProgram Options:")
        print(" 1) Add book")
        print(" 2) Print library books")
        print(" 3) Print books by prefix")
        print(" 4) Add user")
        print(" 5) Borrow book")
        print(" 6) Return book")
        print(" 7) Print users borrowed book")
        print(" 8) Print users")
        print(" 9) Exit")

        try:
            choice = int(input("\nEnter your choice from 1 to 9: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        if choice == 1:
            book_id = input("Please Enter the book id: ")
            name = input("Please Enter the book name: ")
            try:
                quantity = int(input("Please Enter the book quantity: "))
            except ValueError:
                print("Invalid quantity. Must be a number.")
                continue
            admin.add_book(book_id, name, quantity)

        elif choice == 2:
            admin.print_books()

        elif choice == 3:
            prefix = input("Enter book name prefix to search: ")
            admin.print_books_by_prefix(prefix)

        elif choice == 4:
            user_id = input("Please Enter the user id: ")
            name = input("Please Enter the user name: ")
            admin.add_user(user_id, name)

        elif choice == 5:
            user_id = input("Please Enter the user id: ")
            book_id = input("Please Enter the book id: ")
            admin.borrow_book(user_id, book_id)

        elif choice == 6:
            user_id = input("Please Enter the user id: ")
            book_id = input("Please Enter the book id: ")
            admin.return_book(user_id, book_id)

        elif choice == 7:
            user_id = input("Please Enter the user id: ")
            admin.print_users_borrowed_books(user_id)

        elif choice == 8:
            admin.print_users()

        elif choice == 9:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
