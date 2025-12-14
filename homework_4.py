
class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_phone_number(phone_number):
        if phone_number.isdigit() and len(phone_number) == 10:
            return True
        else:
            return False

class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)
        else:
            raise ValueError("Invalid phone number")
        
ContactList.add_contact("Айзат", "1234567890")
ContactList.add_contact("Алина", "0987654321")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)
