class ContactList(list):
    'This class demonstrates inheritance (list) and add search capability for a contact'
    def search(self,name):
        'This function returns take contact name as a string and returns the matching contact'
        matching_contacts=list()
        for contact in self:
            if name in contact.name:
             matching_contacts.append(contact)
        return matching_contacts

class Contact:
    '''This class takes name and email as an argument and create a contact. It also maintains a list
    maintains a list of all the contacts created'''
    all_contacts = ContactList()

    def __init__(self, name , email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    '''This class is the extension of Contact and provides the capability to place an order if the
     contact type is supplier'''
    def order (self, order):
        print("If this was a real system we would send" "'{}' order to '{}'".format(order,self.name))

class Friend (Contact):
    def __init__(self,name,email,phone):
        super().__init__(name,email)
        self.phone = phone

class MailSender:
    def send_email(self,message):
        print("sending email to " +self.email)

class EmailableContact(Contact, MailSender):
    pass