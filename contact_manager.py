# contact_manager.py - Contact Manager Module
# Responsible for maintaining and modifying the contact list

from contact import get_full_name 
from contact import create_contact
import json

contact_list = []

# Function to add a contact to the JSON file
def add_contact(contact):
    saved_contacts = load_contacts()  # Load existing contacts
    saved_contacts.append(contact)  # Append the new contact
    
    # Save the updated contact list back to the JSON file
    with open("contacts.json", "w") as file:
        json.dump(saved_contacts, file, indent=4)
    
    print(contact[0] + " has been added successfully.")

# Function to load contacts from the JSON file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)  # Load contacts from file
    except FileNotFoundError:
        contacts = []  # Return an empty list if file not found
    
    return contacts if isinstance(contacts, list) else []

# Main function to add a sample contact (for testing purposes)
def main():
    contact = {"name": "John Doe", "email": "john@example.com", "phone": "1234567890", "address": "Address"}
    add_contact(contact)

if __name__ == "__main__":
    main()

# Function to display contacts and allow the user to select one to view details
def get_contacts():
    contacts = load_contacts()  # Load contacts from file
    if not contacts:
        print("No contacts found.")
        return
    
    print("Contacts:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact[0]}")  # Display contact names with indices

    choice = input("Enter the number of the contact to see details (or 'q' to quit): ")
    if choice.lower() == 'q':
        return

    try:
        index = int(choice) - 1
        selected_contact = contacts[index]  # Get selected contact
        print_contact(selected_contact)  # Print contact details
    except (ValueError, IndexError):
        print("Invalid choice. Please enter a valid number.")

# Function to print contact details
def print_contact(contact):
    print("\nContact Information:")
    print(f"Name: {contact[0]}")
    print(f"Email: {contact[1]}")
    print(f"Phone: {contact[2]}")
    print(f"Address: {contact[3]}")

# Function to load contacts (repeated function, should be merged)
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)  # Load contacts from file
    except FileNotFoundError:
        contacts = []  # Return an empty list if file not found
    
    return contacts if isinstance(contacts, list) else []

# Main function to repeatedly display contacts and allow viewing details
def main():
    while True:
        get_contacts()
        if input("Do you want to view another contact? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()

# Function to search for a contact by first name
def search_contact(first_name):
    contacts = load_contacts()  # Load contacts from file
    found_contacts = []

    for contact in contacts:
        if contact[0].lower().startswith(first_name.lower()):  # Check if contact's first name matches
            found_contacts.append(contact)  # Add matching contacts to the list

    if not found_contacts:
        print("No contacts found with that first name.")
        return

    for contact in found_contacts:
        print_contact(contact)  # Print matching contacts

# Function to print contact details (repeated function, should be merged)
def print_contact(contact):
    print("\nContact Information:")
    print(f"Name: {contact[0]}")
    print(f"Email: {contact[1]}")
    print(f"Phone: {contact[2]}")
    print(f"Address: {contact[3]}")

# Function to load contacts (repeated function, should be merged)
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)  # Load contacts from file
    except FileNotFoundError:
        contacts = []  # Return an empty list if file not found
    
    return contacts if isinstance(contacts, list) else []

# Main function to search for a contact by first name
def main():
    first_name = input("Enter the first name of the contact you want to search: ")
    search_contact(first_name)

if __name__ == "__main__":
    main()

# Function to display contacts and allow the user to select one to delete
def display_contacts():
    contacts = load_contacts()  # Load contacts from file
    if not contacts:
        print("No contacts found.")
        return

    print("Contacts:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact[0]}")  # Display contact names with indices

    return contacts

# Function to delete a selected contact
def delete_contact():
    contacts = display_contacts()  # Display contacts
    if not contacts:
        return

    choice = input("Enter the number of the contact to delete (or 'q' to quit): ")
    if choice.lower() == 'q':
        return

    try:
        index = int(choice) - 1
        deleted_contact = contacts.pop(index)  # Remove selected contact
        
        # Save updated contact list back to the JSON file
        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=4)
        
        print(f"{deleted_contact[0]} has been deleted successfully.")
    except (ValueError, IndexError):
        print("Invalid choice. Please enter a valid number.")

# Main function to repeatedly delete contacts
def main():
    while True:
        delete_contact()
        if input("Do you want to delete another contact? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
