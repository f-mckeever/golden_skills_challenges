from lib.diary import *
"""
Diary can be instantiated
"""

def test_diary_instantiated():
    diary = Diary()
    assert isinstance(diary, Diary)