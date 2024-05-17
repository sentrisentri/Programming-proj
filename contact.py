# contact.py - Contact Module
# Responsible for creating a contact record

# You may add extra fields to the contact record
def create_contact(fname, lname, phone, email):

    saved_contact = {
         "First Name": fname,
         "Last Name": lname,
         "Phone Number": phone,
         "Email": email
         }
    return saved_contact
    
   
def get_full_name(contact):
    return contact["First Name"] + " " + contact["Last Name"]

def display_contact(contact):
 return  
  
def input_contact():
    return




