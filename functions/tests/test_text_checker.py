from lib.text_checker import *
import pytest
#Given a text   -> validate that it starts with a capital letter
#               -> validate that it ends with a sentence-ending punctuation mark
#               -> . ! ? 
#Minimum length for a text will have to be 2 ? one capital letter and one punctuation mark

#Text is valid, correct capital letter and correct punctuation mark
def test_text_checker_valid():
    valid_text = "Hello, Stacy.  Did you hear about Abbey crashing a car into the bowling alley?"
    result = text_checker(valid_text)
    assert result

def test_text_checker_invalid_no_capital_start():
    invalid_text = "wagwan, my friend."
    result = text_checker(invalid_text)
    assert not result

def test_text_checker_invalid_no_punctuation_end():
    invalid_text = "There's the biggest armadillo I've ever seen in my fucking life outside the back gate right now"
    result = text_checker(invalid_text)
    assert not result


#Text is 2 characters or less, ie cant check both a capital letter and a punctuation mark
def test_text_checker_invalid_too_short():
    empty_text = ""
    with pytest.raises(Exception) as e:
        result = text_checker(empty_text)
    error_message = str(e.value)
    assert error_message == "Text is too short to check."

def test_text_starts_capital_valid():
    text = "Hello"
    result = text_starts_with_capital(text)
    assert result

def test_text_starts_capital_invalid():
    text = "hello"
    result = text_starts_with_capital(text)
    assert not result

def test_text_ends_punctuation_valid():
    text = "yabbadabbadoo?"
    result = text_ends_punctuation(text)
    assert True
    text = "yabbadabbadoo!"
    result = text_ends_punctuation(text)
    assert True
    text = "yabbadabbadoo."
    result = text_ends_punctuation(text)
    assert True