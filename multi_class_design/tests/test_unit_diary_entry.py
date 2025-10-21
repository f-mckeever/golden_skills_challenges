from lib.diary_entry import *
import pytest
"""
Given a valid title and contents, #get_title returns the title
"""

def test_de_valid_get_title():
    de = DiaryEntry("Title", "Contents")
    result = de.get_title()
    assert result == "Title"

"""
Given a valid title and contents, #get_contents returns the contents
"""

def test_de_valid_get_title():
    de = DiaryEntry("Title", "Contents")
    result = de.get_contents()
    assert result == "Contents"


"""
Given an empty string for title or contents, raises exception
"""

def test_de_invalid_empty_string_params():
    #empty title
    with pytest.raises(Exception) as e:
        de = DiaryEntry("", "Contents")
    err_msg = str(e.value)
    assert err_msg == "Title and contents must not be empty strings."

    #empty contents
    with pytest.raises(Exception) as e:
        de = DiaryEntry("Title", "")
    err_msg = str(e.value)
    assert err_msg == "Title and contents must not be empty strings."

    #empty both
    with pytest.raises(Exception) as e:
        de = DiaryEntry("", "")
    err_msg = str(e.value)
    assert err_msg == "Title and contents must not be empty strings."

"""
Given a non string value for title or contents, raises exception
"""

def test_de_invalid_non_string_params():
    #non string title
    with pytest.raises(Exception) as e:
        de = DiaryEntry(69, "Contents")
    err_msg = str(e.value)
    assert err_msg == "Title and contents must be strings."

    #non string contents
    with pytest.raises(Exception) as e:
        de = DiaryEntry("Title", None)
    err_msg = str(e.value)
    assert err_msg == "Title and contents must be strings."

    #non string both
    with pytest.raises(Exception) as e:
        de = DiaryEntry(False, 473892.432)
    err_msg = str(e.value)
    assert err_msg == "Title and contents must be strings."

"""
Count_words returns the number of words in contents - 10 words
"""

def test_de_count_words_10_length_returns_10():
    de = DiaryEntry("Title", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10.")
    result = de.count_words()
    assert result == 10

"""
Count_words returns the number of words in contents - 8 words
"""

def test_de_count_words_10_length_returns_10():
    de = DiaryEntry("Title", "1, 2, 3, 4, 5, 6, 7, 8.")
    result = de.count_words()
    assert result == 8

"""
Count_words returns the number of words in contents - 3 words
"""

def test_de_count_words_10_length_returns_10():
    de = DiaryEntry("Title", "1, 2, 3.")
    result = de.count_words()
    assert result == 3

"""
Given a valid wpm-> #reading_time returns time in minutes it takes to read the entry
"""

def test_de_reading_time_valid_params():
    #10 words
    de = DiaryEntry("Title", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12.")
    wpm = 12
    #expected output 1
    result = de.reading_time(wpm)
    assert result == 1


    wpm = 3
    #expceted output 4
    result = de.reading_time(wpm)
    assert result == 4

    wpm = 6
    #expected output 2
    result = de.reading_time(wpm)
    assert result == 2

"""
Given a wpm less than or equal to 0, raises exception
"""

def test_de_reading_time_invalid_wpm_less_than_1():
    de = DiaryEntry("Title", "1, 2, 3, 4, 5.")
    wpm = 0
    with pytest.raises(Exception) as e:
        de.reading_time(wpm)
    err_msg = str(e.value)
    assert err_msg == "Wpm must be greater than 0."

"""
Given a non int wpm, raises exception
"""

def test_de_reading_time_invalid_wpm_non_int():
    de = DiaryEntry("Title", "1, 2, 3, 4, 5.")
    wpm = "Fish"
    with pytest.raises(Exception) as e:
        de.reading_time(wpm)
    err_msg = str(e.value)
    assert err_msg == "Wpm must be an integer."

    wpm = True
    with pytest.raises(Exception) as e:
        de.reading_time(wpm)
    err_msg = str(e.value)
    assert err_msg == "Wpm must be an integer."

    wpm = 543.123
    with pytest.raises(Exception) as e:
        de.reading_time(wpm)
    err_msg = str(e.value)
    assert err_msg == "Wpm must be an integer."