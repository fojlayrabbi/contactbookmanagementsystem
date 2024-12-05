from contact_operations import add_contact, view_contacts, remove_contact, search_contacts
from file_operations import load_contacts, save_contacts

def main():
    filename = "contacts.txt"
    contacts = load_contacts(filename)
    
    while True:
        print("\nContact Book Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_contact(contacts)
            save_contacts(filename, contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            remove_contact(contacts)
            save_contacts(filename, contacts)
        elif choice == "4":
            search_contacts(contacts)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
