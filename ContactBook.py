class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}\n{'-' * 30}"


class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact
        print(f"Contact '{contact.name}' added successfully.")

    def view_contacts(self):
        print("Contact List:")
        for name, contact in self.contacts.items():
            print(contact)

    def search_contact(self, query):
        found = False
        for name, contact in self.contacts.items():
            if query in name or query in contact.phone:
                print(contact)
                found = True
        if not found:
            print("Contact not found.")

    def update_contact(self, name, new_contact):
        if name in self.contacts:
            self.contacts[name] = new_contact
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")


def main():
    print("Welcome to the Interactive Contact Book Adventure!")

    contact_book = ContactBook()

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Great! Let's add a new contact.")
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)

        elif choice == "2":
            print("Here's your contact list:")
            contact_book.view_contacts()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            contact_book.search_contact(query)

        elif choice == "4":
            name = input("Enter name of contact to update: ")
            if name in contact_book.contacts:
                print(f"Updating contact '{name}'.")
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                updated_contact = Contact(name, phone, email, address)
                contact_book.update_contact(name, updated_contact)
            else:
                print(f"Contact '{name}' not found.")

        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == "6":
            print("Thank you for using the Interactive Contact Book Adventure!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
