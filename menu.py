# menu.py - Menu Module
# Responsible for displaying and implementing the menu options

from contact_manager import get_contacts, add_contact, search_contact, delete_contact

from contact import display_contact, input_contact

def display_menu():
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Quit")

def option_1():
    # display_contacts():
    print("Displaying Contacts...")

def option_2():
    # add_contact():
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    contact = [fname, lname, phone, email]
    add_contact(contact)
    

def option_3():
    # search_contact():
    print("Search Contact")

def option_4():
    # delete_contact():
    print("Delete Contact")
    
