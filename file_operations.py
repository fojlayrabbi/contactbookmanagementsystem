# Load contacts from a file
def load_contacts(filename):
    contacts = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, email, phone, address = line.strip().split(", ")
                contacts.append({"name": name, "email": email, "phone": phone, "address": address})
    except FileNotFoundError:
        # If the file does not exist, start with an empty contact list
        pass
    return contacts

# Save contacts to a file
def save_contacts(filename, contacts):
    with open(filename, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']}, {contact['email']}, {contact['phone']}, {contact['address']}\n")
