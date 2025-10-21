from lib.contact_list import *

"""
ContactList instantiates
"""

def test_contact_list_instantiates_with_empty_list():
    cl = ContactList()
    assert isinstance(cl, ContactList)
    assert cl.contact_list == []