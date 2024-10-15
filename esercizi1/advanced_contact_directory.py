class Contact:
    contacts = []

    def __init__(self, name, phone, email, notes=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.notes = notes
        Contact.contacts.append(self)

    def display_details(self):
        print(f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Notes: {self.notes}")

    def update_notes(self, new_notes):
        self.notes = new_notes

    @classmethod
    def create_default_contact(cls):
        return cls("John Doe", "3452180324", "johndoe@gmail.com", "Default contact")

    @staticmethod
    def search_by_name(name):
        for contact in Contact.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

contact1 = Contact("Mario Rossi", "342567654", "mario.rossi@gmail.com", "Work colleague")
contact2 = Contact.create_default_contact()

contact1.display_details()
contact2.display_details()

contact1.update_notes("Long-time friend")
contact1.display_details()

search_result = Contact.search_by_name("Mario Rossi")
if search_result:
    print("Contact found:")
    search_result.display_details()
else:
    print("Contact not found.")
