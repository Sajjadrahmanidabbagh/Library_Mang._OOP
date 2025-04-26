"""
Created on Sat Jan 4 2024

@author: sajjad
"""

from LibraryManager import *

class LibraryAssistant:
    def __init__(self):
        self.manager = LibraryManager()
    def display_menu(self):
        print("Menu Options:")
        options = [
            '1) Register a book',
            '2) Show all titles',
            '3) Search titles by prefix',
            '4) Register a member',
            '5) Issue a title',
            '6) Receive a returned title',
            '7) View borrowed titles by members',
            '8) List all members'
        ]
        print('\n'.join(options))
        return self.get_selection(len(options))
    def get_selection(self, max_options):
        prompt = f"Select an option between 1 and {max_options}: \n"
        return validate_input(prompt, 1, max_options)
    def register_book(self):
        catalog_id = input('Enter book ID: \n')
        title = input('Enter book title: \n')
        stock = input('Enter book stock quantity: \n')
        self.manager.register_book(catalog_id, title, stock)
    def show_titles(self):
        print(self.manager.display_books())

    def find_titles(self):
        keyword = input('Enter search prefix: \n')
        print(', '.join(self.manager.find_book(keyword)))
    def register_member(self):
        member_id = int(input('Enter member ID: \n'))
        member_name = input('Enter member name: \n')
        self.manager.register_member(member_id, member_name)
    def issue_title(self):
        member_name = input('Enter member name: \n')
        title = input('Enter title name: \n') 
        self.manager.lend_book(member_name, title)
    def receive_title(self):
        member_name = input('Enter member name: \n')
        title = input('Enter title name: \n')
        self.manager.return_title(member_name, title)
    def view_borrowed_titles(self):
        self.manager.list_borrowers()
    def list_members(self):
        self.manager.list_all_members()
    def execute(self):
        while True:
            choice = self.display_menu()

            if choice == 1:
                self.register_book()
            elif choice == 2:
                self.show_titles()
            elif choice == 3:
                self.find_titles()
            elif choice == 4:
                self.register_member()
            elif choice == 5:
                self.issue_title()
            elif choice == 6:
                self.receive_title()
            elif choice == 7:
                self.view_borrowed_titles()
            elif choice == 8:
                self.list_members()
            else:
                print("Program terminated.")
                break
