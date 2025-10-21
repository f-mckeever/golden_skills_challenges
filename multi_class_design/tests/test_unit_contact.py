from lib.contact import *
import pytest

"""
Given a valid name and number, #get_contact returns that name and number
"""

def test_contact_get_contact_valid_params():
    contact = Contact("Bradley", "+447462896475")
    result = contact.get_contact()
    assert result == "Bradley, +447462896475"


"""
Given an empty string, raises exception
"""

def test_contact_invalid_params_empty_string():
    with pytest.raises(Exception) as e:
        contact = Contact("", "")
    err_msg = str(e.value)
    assert err_msg == "Name and number cannot be empty strings."

"""
Given a non string, raises exception
"""

def test_contact_invalid_params_non_string():
    with pytest.raises(Exception) as e:
        contact = Contact(5, "")
    err_msg = str(e.value)
    assert err_msg == "Name and number must be strings."