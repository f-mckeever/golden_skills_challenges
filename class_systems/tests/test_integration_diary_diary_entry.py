from lib.diary import *
from lib.diary_entry import *
import pytest
"""
Given a diary entry, the entry is added to a list of entries and returned by #all
"""

def test_add_diary_entry_valid():
    diary = Diary()
    de = DiaryEntry("Title", "Contents")
    diary.add(de)
    result = diary.all()
    assert result == [de]

def test_add_diary_entry_non_diary():
    diary = Diary()
    de = "Fart"
    with pytest.raises(Exception) as e:
        diary.add(de)
    error_message = str(e.value)
    assert error_message == "Entry must be an instance of DiaryEntry."
 
def test_count_words_returns_count():
    diary = Diary()
    de1 = DiaryEntry("Title", "1, 2, 3, 4, 5.")
    de2 = DiaryEntry("Title", "1, 2, 3, 4, 5.")
    de3 = DiaryEntry("Title", "1, 2, 3, 4, 5.")
    diary.add(de1)
    result = diary.count_words()
    assert result == 5

    diary.add(de2)
    result = diary.count_words()
    assert result == 10

    diary.add(de3)
    result = diary.count_words()
    assert result == 15

def test_reading_time_valid_wpm():
    diary = Diary()
    de1 = DiaryEntry("Title", "1, 2, 3, 4, 5.")
    de2 = DiaryEntry("Title", "1, 2, 3, 4, 5.")
    de3 = DiaryEntry("Title", "1, 2, 3, 4, 5.")
    diary.add(de1)
    diary.add(de2)
    diary.add(de3)

    wpm = 3
    result = diary.reading_time(wpm)
    assert result == 5

    wpm = 5
    result = diary.reading_time(wpm)
    assert result == 3

def test_reading_time_invalid_wpm_below_1():
    diary = Diary()
    de1 = DiaryEntry("Title", "1, 2, 3, 4, 5.")
    de2 = DiaryEntry("Title", "1, 2, 3, 4, 5.")
    de3 = DiaryEntry("Title", "1, 2, 3, 4, 5.")
    diary.add(de1)
    diary.add(de2)
    diary.add(de3)

    wpm = 0

    with pytest.raises(Exception) as e:
        result = diary.reading_time(wpm)
    error_message = str(e.value)
    assert error_message == "Wpm must be greater than 0."

def test_reading_time_invalid_wpm_non_int():
    diary = Diary()
    de1 = DiaryEntry("Title", "1, 2, 3, 4, 5.")
    de2 = DiaryEntry("Title", "1, 2, 3, 4, 5.")
    de3 = DiaryEntry("Title", "1, 2, 3, 4, 5.")
    diary.add(de1)
    diary.add(de2)
    diary.add(de3)

    wpm = False

    with pytest.raises(Exception) as e:
        result = diary.reading_time(wpm)
    error_message = str(e.value)
    assert error_message == "Wpm must be an integer."

def test_best_entry_returns_entry_with_word_count_price_is_right_rules():
    diary = Diary()
    de1 = DiaryEntry("Title", "1, 2, 3.")
    de2 = DiaryEntry("Title", "1, 2, 3, 4, 5, 6, 7.")
    de3 = DiaryEntry("Title", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10.")
    
    wpm = 9
    minutes = 1

    diary.add(de1)
    diary.add(de2)
    diary.add(de3)
    
    result = diary.find_best_entry_for_reading_time(wpm, minutes)
    assert result == de2

def test_all_methods_for_empty_entries_list():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.count_words()
    error_message = str(e.value)
    assert error_message == "Entries list is currently empty."

    with pytest.raises(Exception) as e:
        diary.reading_time(5)
    error_message = str(e.value)
    assert error_message == "Entries list is currently empty."

    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(5, 10)
    error_message = str(e.value)
    assert error_message == "Entries list is currently empty."

def test_best_entry_invalid_parameters():
    diary = Diary()
    de1 = DiaryEntry("Title", "Contents")
    de2 = DiaryEntry("Title", "Contents")
    de3 = DiaryEntry("Title", "Contents")
    diary.add(de1)
    diary.add(de2)
    diary.add(de3)

    #wpm <= 0 
    wpm = 0
    minutes = 1
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(wpm, minutes)
    error_message = str(e.value)
    assert error_message == "Wpm and minutes must be greater than 0."


    #minutes <= 0
    wpm = 2
    minutes = -5
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(wpm, minutes)
    error_message = str(e.value)
    assert error_message == "Wpm and minutes must be greater than 0."


    #wpm non int
    wpm = 5442.312431
    minutes = 1
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(wpm, minutes)
    error_message = str(e.value)
    assert error_message == "Wpm and minutes must be an integer."


    #minutes non int
    wpm = 1
    minutes = False
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(wpm, minutes)
    error_message = str(e.value)
    assert error_message == "Wpm and minutes must be an integer."