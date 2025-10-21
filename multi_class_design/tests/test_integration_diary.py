import pytest
from lib.diary_entry import *
from lib.diary import *
from lib.task_list import *
from lib.contact_list import *
from lib.contact import *
from lib.task import *

"""
Given valid diary entries
#entries returns a list of diary entries
"""

def test_diary_add_adds_entries_to_list():
    d = Diary()
    assert d.entry_list == []
    de1 = DiaryEntry("Title", "Contents")
    de2 = DiaryEntry("Title", "Contents")
    de3 = DiaryEntry("Title", "Contents")

    d.add_entry(de1)
    d.add_entry(de2)
    d.add_entry(de3)

    assert d.entries() == [de1, de2, de3]

"""
Given non diaryentry instances
#add_entry raises exception
"""

def test_de_add_invalid_params_non_diaryentry():
    d = Diary()
    with pytest.raises(Exception) as e:
        d.add_entry("fart")
    err_msg = str(e.value)
    assert err_msg == "Entry must be an instance of DiaryEntry."

"""
Give self.entry_list is empty
#entries raises exception
"""
def test_de_entry_list_empty_list_exception():
    d = Diary()
    with pytest.raises(Exception) as e:
        d.entries()
    err_msg = str(e.value)
    assert err_msg == "Entry list is currently empty."

"""
#tasks returns list of tasks
"""
def test_de_tasks_returns_list_of_tasks():
    d = Diary()
    assert isinstance(d.task_list, TaskList)

    with pytest.raises(Exception) as e:
        d.tasks()
    err_msg = str(e.value)
    assert err_msg == "Task list is currently empty."

    t1 = Task("Wipe out the humans.")
    t2 = Task("Regret.")
    d.task_list.add(t1)
    d.task_list.add(t2)

    assert d.tasks() == [t1, t2]



"""
#contacts returns list of contacts
"""
def test_de_contacts_returns_list_of_contacts():
    d = Diary()
    assert isinstance(d.contact_list, ContactList)

    with pytest.raises(Exception) as e:
        d.contacts()
    err_msg = str(e.value)
    assert err_msg == "Contact list is currently empty."

    c1 = Contact("Wally", "+447354977651")
    c2 = Contact("Regret", "+447123649841")
    d.contact_list.add(c1)
    d.contact_list.add(c2)

    assert d.contacts() == [c1, c2]


def test_best_entry_returns_entry_with_word_count_price_is_right_rules():
    diary = Diary()
    de1 = DiaryEntry("Title", "1, 2, 3.")
    de2 = DiaryEntry("Title", "1, 2, 3, 4, 5, 6, 7.")
    de3 = DiaryEntry("Title", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10.")
    
    wpm = 9
    minutes = 1

    diary.add_entry(de1)
    diary.add_entry(de2)
    diary.add_entry(de3)
    
    result = diary.best_entry(wpm, minutes)
    assert result == de2

def test_best_entry_invalid_parameters():
    diary = Diary()
    de1 = DiaryEntry("Title", "Contents")
    de2 = DiaryEntry("Title", "Contents")
    de3 = DiaryEntry("Title", "Contents")
    diary.add_entry(de1)
    diary.add_entry(de2)
    diary.add_entry(de3)

    #wpm <= 0 
    wpm = 0
    minutes = 1
    with pytest.raises(Exception) as e:
        diary.best_entry(wpm, minutes)
    error_message = str(e.value)
    assert error_message == "Wpm and minutes must be greater than 0."


    #minutes <= 0
    wpm = 2
    minutes = -5
    with pytest.raises(Exception) as e:
        diary.best_entry(wpm, minutes)
    error_message = str(e.value)
    assert error_message == "Wpm and minutes must be greater than 0."


    #wpm non int
    wpm = 5442.312431
    minutes = 1
    with pytest.raises(Exception) as e:
        diary.best_entry(wpm, minutes)
    error_message = str(e.value)
    assert error_message == "Wpm and minutes must be an integer."


    #minutes non int
    wpm = 1
    minutes = False
    with pytest.raises(Exception) as e:
        diary.best_entry(wpm, minutes)
    error_message = str(e.value)
    assert error_message == "Wpm and minutes must be an integer."
