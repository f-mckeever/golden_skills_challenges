from lib.grammar_stats import *
import pytest
"""
GrammarStats.check(string) -> will return true if string starts with capital letter
and ends with sentence ending punctuation mark

False if either condition not met

Error if text not a string

Error if text shorter than 2 characters

text = "Hello." -> returns True



GrammarStats percentage_good
-> returns int
-> int equates to percentage of total texts checked that have passed the check
-> REQUIRES TOTAL TEXTS AND PASSED TEXT TRACKING
"""
#check
def test_text_correct_grammar_returns_true():
    gs = GrammarStats()
    text = "Hello."
    result = GrammarStats().check(text)
    assert result == True

def test_text_start_no_capital_returns_false():
    gs = GrammarStats()
    text = "hello."
    result = GrammarStats().check(text)
    assert result == False

def test_text_ends_no_punctuation_returns_false():
    gs = GrammarStats()
    text = "Hello"
    result = GrammarStats().check(text)
    assert result == False

def test_text_not_string_raises_error():
    gs = GrammarStats()
    text = 69
    with pytest.raises(Exception) as e:
        result = GrammarStats().check(text)
    error_message = str(e.value)
    assert error_message == "Text must be a string."

def test_text_less_than_two_characters_raises_error():
    gs = GrammarStats()
    text = "a"
    with pytest.raises(Exception) as e:
        result = GrammarStats().check(text)
    error_message = str(e.value)
    assert error_message == "Text must be longer than 2 characters in order to be evaluated."

# percentage_good
def test_percentage_good_returns_int():
    gs = GrammarStats()
    result = gs.percentage_good()
    assert type(result) == int

def test_percentage_good_returns_percentage_1_correct_text_returns_100():
    gs = GrammarStats()
    correct_text = "Hello."
    gs.check(correct_text)

    print(gs.total_texts)

    result = gs.percentage_good()
    assert result == 100

def test_percentage_good_returns_percentage_1_correct_text_1_wrong_text_returns_50():
    gs = GrammarStats()
    correct_text = "Hello."
    incorrect_text = "fart"
    gs.check(correct_text)
    gs.check(incorrect_text)
    result = gs.percentage_good()
    assert result == 50

def test_percentage_good_returns_percentage_all_texts_wrong_returns_0():
    gs = GrammarStats()
    incorrect_text1 = "Hhfr7ew9ahello"
    incorrect_text2 = "Dart"
    incorrect_text3 = "idfuhsofu8eareu."

    gs.check(incorrect_text1)
    gs.check(incorrect_text2)
    gs.check(incorrect_text3)

    result = gs.percentage_good()
    assert result == 0

def test_percentage_good_returns_percentage_1_correct_text_2_incorrect_texts_returns_int():
    gs = GrammarStats()
    correct_text = "Hhfr7ew9ahello."
    incorrect_text1 = "Dart"
    incorrect_text2 = "idfuhsofu8eareu."

    gs.check(correct_text)
    gs.check(incorrect_text1)
    gs.check(incorrect_text2)

    result = gs.percentage_good()
    assert result == 33