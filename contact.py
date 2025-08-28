import json
from datetime import datetime

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.filename = "contacts.json"
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=2)

    def add_contact(self):
        contact = {
            "name": input("Enter name: "),
            "phone": input("Enter phone number: "),
            "email": input("Enter email: "),
            "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.contacts.append(contact)
        self.save_contacts()
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found!")
            return
        
        print("\nContact List:")
        for idx, contact in enumerate(self.contacts, 1):
            print(f"\n{idx}. Name: {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print(f"   Added: {contact['date_added']}")

    def search_contact(self):
        search_term = input("Enter name to search: ").lower()
        found = False
        for contact in self.contacts:
            if search_term in contact['name'].lower():
                print(f"\nFound: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                found = True
        if not found:
            print("No matching contacts found!")

    def delete_contact(self):
        self.view_contacts()
        if not self.contacts:
            return
        
        try:
            idx = int(input("Enter number of contact to delete: ")) - 1
            if 0 <= idx < len(self.contacts):
                removed = self.contacts.pop(idx)
                self.save_contacts()
                print(f"Deleted contact: {removed['name']}")
            else:
                print("Invalid contact number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    manager = ContactManager()
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ")
        
        if choice == '1':
            manager.add_contact()
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            manager.search_contact()
        elif choice == '4':
            manager.delete_contact()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
