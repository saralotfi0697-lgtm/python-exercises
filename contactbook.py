class Contact:
    def __init__(self,name , phone):
        self.name=name
        self.phone=phone
    def __str__(self):
        return (f'Contact_Name:{self.name}-Contact_Phone:{self.phone}')
    def show_info(self):
        return (f'Contact_Name:{self.name}-Contact_Phone:{self.phone}')
class Contactbook:
    def __init__(self):
        self.contacts=[]
    def add_contact(self,name,phone):
        c=Contact(name,phone)
        self.contacts.append(c)
    def show_all(self):
        for contact in self.contacts:
            print(contact.show_info())
    def search_contact(self,name):
        for contact in self.contacts:
            if contact.name.lower()==name.lower():
                return contact.show_info()
        return "This Contact Not Found."
    def __len__(self):
        return len(self.contacts)
oc=Contact('Zahra',198)
ob=Contactbook()
ob.add_contact('Sara',123)
ob.add_contact('Mina',456)
ob.add_contact('Sina',789)
print(ob.search_contact('sara'))
print(ob.search_contact('reza'))
print('----')
print(oc)
ob.show_all()
print(len(ob))

        