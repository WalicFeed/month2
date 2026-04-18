class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
    @staticmethod
    def validate_phone_number(phone_number):
        return len(phone_number) == 10 and phone_number.isdigit()

class ContactList:
    all_contacts = []
    @classmethod
    def add_contact(cls,name, phone_number):
        if Contact.validate_phone_number(phone_number):
            contact = Contact(name, phone_number)
            cls.all_contacts.append(contact)
        else:
            raise ValueError("Phone number must be 10 numbers long.")

class Library:
    def __init__(self, city, books = None):
        self.city = city
        self.books = books
    def __str__(self):
        return f"<Library object, city:{self.city}, books: {len(self.books)}>"
    def __len__(self):
        return len(self.books)
    def __contains__(self, chosen_one):
        return chosen_one in self.books
    def __bool__(self):
        return len(self.books) > 5