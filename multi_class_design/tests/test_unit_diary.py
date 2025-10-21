from lib.diary import *
"""
Diary instantiates
"""
def test_diary_instantiates():
    diary = Diary()
    assert isinstance(diary, Diary)