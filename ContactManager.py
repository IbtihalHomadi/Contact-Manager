
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.phone}) ({self.email})"


class ContactManager:
    def __init__(self):
        self.contacts_list = []

    def add_contact(self):
        name = input("Enter Contact's Name : ")
        phone = input("Enter Contact's Phone Number : ")
        email = input("Enter Contact's Email")

        contact = Contact(name, phone_number, email_address)
        self.contacts_list.append(contact)

    def remove_contact(self, name):
        contact = self.search_contact(name)
        if contact:
            self.contacts_list.remove(contact)
            return True
        return False

    def search_contact(self, name):
        for contact in self.contacts_list:
            if contact.name == name:
                print(contact)
        return None

    def display_contacts(self):
        for contact in self.contacts_list:
            return contact
        return "No contacts found"


if __name__ == "__main__":
    contact_manager = ContactManager()

    while True:
        print("Contact Manager")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display Contact")
        print("5. Exit")

        choice = input("Enter your Choice: ")
        if choice == "1":
            contact_manager.add_contact()
        elif choice == "2":
            name = input("Enter the Contact's name:")
            contact_manager.remove_contact(name)

        elif choice == "3":
            name = input("Enter Contact's Name: ")
            contact_manager.search_contact(name)
            '''contact = contact_manager.search_contact(name)
            if contact:
                print(contact)
            else:
                print("Contact not found")'''

        elif choice == "4":
            contact_manager.display_contacts()
        elif choice == "5":
            break
        else:
            print("Invalid choice")