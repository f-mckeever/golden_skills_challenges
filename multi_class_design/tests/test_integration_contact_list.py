import pytest
from lib.contact import *
from lib.contact_list import *

"""
Given valid contacts
#get_contact_list returns a list of contacts
"""

def test_contactlist_add_and_get_contact_list():
    cl = ContactList()
    c1 = Contact("Carl", "+447836264552")
    c2 = Contact("Barl", "+447923540016")
    c3 = Contact("Marl", "+447555438712")

    assert cl.contact_list == []

    cl.add(c1)
    cl.add(c2)
    cl.add(c3)

    assert cl.contact_list == [c1, c2, c3]

"""
Given contact_list is empty,
#get_contact_list raises exception
"""

def test_contactlist_get_contact_list_empty_list_exception():
    cl = ContactList()
    with pytest.raises(Exception) as e:
        cl.get_contact_list()
    err_msg = str(e.value)
    assert err_msg == "Contact list is currently empty."


"""
Given an invalid contact, 
#add raises an exception
"""

def test_contactlist_add_contact_invalid_params_non_contact():
    cl = ContactList()
    with pytest.raises(Exception) as e:
        cl.add(54321)
    err_msg = str(e.value)
    assert err_msg == "Contact must be an instance of Contact."