# menu.py - Menu Module
# Responsible for displaying and implementing the menu options

from contact_manager import get_contacts, add_contact, search_contact, delete_contact
import json

# Function to display the main menu
def display_menu():
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Quit")

# Option 1: Display all contacts
def option_1():
    get_contacts()

# Option 2: Add a new contact
def option_2():
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    contact = [fname, lname, phone, email]  # Create a contact list
    add_contact(contact)  # Add the contact to the contact list

# Option 3: Search for a contact by first name
def option_3():
    name = input("Type the first name you want to search: ")
    search_contact(name)

# Option 4: Delete a contact
def option_4():
    delete_contact()
