# Add a new contact
def add_contact(contacts):
    name = input("Enter Name: ").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone Number: ").strip()
    address = input("Enter Address: ").strip()
    
    # Validate input
    if not name.isalpha():
        print("Error: Name must contain only letters.")
        return
    if not phone.isdigit():
        print("Error: Phone number must be numeric.")
        return
    if any(contact['phone'] == phone for contact in contacts):
        print("Error: Phone number already exists.")
        return
    
    # Add the new contact
    contacts.append({"name": name, "email": email, "phone": phone, "address": address})
    print("Contact added successfully.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\nContacts:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")

# Remove a contact by phone number
def remove_contact(contacts):
    phone = input("Enter the phone number of the contact to remove: ").strip()
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("Contact removed successfully.")
            return
    print("Contact not found.")

# Search for contacts
def search_contacts(contacts):
    search_term = input("Enter name, email, or phone to search: ").strip().lower()
    results = [contact for contact in contacts if search_term in contact['name'].lower() or
               search_term in contact['email'].lower() or
               search_term in contact['phone']]
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
    else:
        print("No contacts found.")
