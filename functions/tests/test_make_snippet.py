from lib.make_snippet import *
#Given an empty string, it will return an empty string

#Given string of 5 words or less, it will return the same string

#Given a string of more than 5 words, it will return the first 5 words from the string, followed by ...

def test_make_snippet_empty_string_returns_empty_string():
    string = ""
    result = make_snippet(string)
    assert result == ""

def test_make_snippet_string_up_to_5_words_returns_string():
    string = "Hello, my name is Fionn."
    result = make_snippet(string)
    assert result == "Hello, my name is Fionn."

def test_make_snippet_string_greater_than_5_words_returns_first_5_and_ellipsis():
    string = "Hello, my name is Fionn and I'm learning Test-driven development :)"
    result = make_snippet(string)
    assert result == "Hello, my name is Fionn..."