from lib.contact import *

class ContactList():
    #init
    #params -> none
    #returns -> none
    #sides -> instantiates self, contact_list = []
    def __init__(self):
        self.contact_list = []

    #add
    #params -> contact: Contact
    #returns -> none
    #sides -> appends contact to self.contacts_list
    def add(self, contact):
        if type(contact) == Contact:
            self.contact_list.append(contact)
        else:
            raise Exception("Contact must be an instance of Contact.")

    #get_contact_list
    #params -> none
    #returns -> self.contact_list, after updating
    #sides -> none
    def get_contact_list(self):
        if len(self.contact_list) > 0:
            return self.contact_list
        else:
            raise Exception("Contact list is currently empty.")

