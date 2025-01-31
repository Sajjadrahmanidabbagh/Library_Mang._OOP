#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:11:04 2024

@author: sajjad
"""

class LibraryManager:
    def __init__(self):
        self.catalog = []  # book object
        self.members = {}  # member object as a key

    def register_book(self, catalog_id, title, stock):
        for item in self.catalog:
            if item.id == catalog_id:
                return print("This title already exists in the catalog")
        new_entry = Book(catalog_id, title, stock)
        self.catalog.append(new_entry)
        print("Book successfully registered")

    def display_books(self):
        titles = [entry.name for entry in self.catalog]
        if not titles:
            return "No titles available"
        return ", ".join(titles)

    def find_book(self, keyword):
        matching_books = [entry.name for entry in self.catalog if entry.name[:len(keyword)].upper() == keyword.upper()]
        if not matching_books:
            return "No matching titles found"
        return matching_books

    def register_member(self, member_id, member_name):
        if member_id in [person.id for person in self.members]:
            return print("This member already exists!")
        new_member = User(member_id, member_name)
        self.members[new_member] = []
        print("Member successfully registered!")
        

    def lend_book(self, member_name, book_title):
        target_book = ''.join(self.find_book(book_title))
        member_exists = False
        available_books = [entry for entry in self.catalog if entry.name == target_book and entry.quantity > 0]
        if not available_books:
            return print("Insufficient stock!")
        available_books[0].quantity -= 1
        for person, borrowed_titles in self.members.items():
            if person.name.lower() == member_name.lower():
                borrowed_titles.append(book_title)
                member_exists = True
        if not member_exists:
            return print("No member found with this name")
        return print(f"{member_name} has borrowed {target_book}")

    def return_title(self, member_name, book_title):
        target_book = ''.join(self.find_book(book_title))
        member_exists = False
        available_books = [entry for entry in self.catalog if entry.name == target_book]
        if not available_books:
            return print("Title not found in catalog")
        available_books[0].quantity += 1
        for person, borrowed_titles in self.members.items():
            if person.name.lower() == member_name.lower():
                if book_title in borrowed_titles:
                    borrowed_titles.remove(book_title)
                member_exists = True
        if not member_exists:
            return print("No member found with this name")
        return print(f"{member_name} has returned {target_book}")

    def list_borrowers(self):
        active_members = [person for person, borrowed_titles in self.members.items() if borrowed_titles]
        if active_members:
            for person in active_members:
                print(f"{person.name} currently borrowed: {', '.join(self.members[person])}")
        else:
            print("No active borrowers at the moment")

    def list_all_members(self):
        member_names = [person.name for person in self.members]
        if member_names:
            print("Registered Members:", ", ".join(member_names))
        else:
            print("No members registered")
