# contact_manager.py - Contact Manager Module
# Responsible for maintaining and modifying the contact list

from contact import get_full_name 
from contact import create_contact
import json

contact_list = []

def add_contact(contact):
    
    saved_contact = create_contact(contact[0], contact[1], contact[2], contact[3])
    json.dump(saved_contact , open("contacts.json", "a"))
    print(contact)
    print( contact[0] + " has been Added Successfully.")

def get_contacts():
    print("Displaying Contacts...")

def search_contact(query):
    print("Searching for contact...")

def delete_contact(contact):
    print("Deleting contact...")
