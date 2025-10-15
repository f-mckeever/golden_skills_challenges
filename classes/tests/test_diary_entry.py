from lib.diary_entry import *
import pytest

#instantiate the diary
def test_diary_entry_instantiate_valid():
    title = "My Title"
    contents = "These are the contents"
    diary_entry = DiaryEntry(title, contents)
    assert isinstance(diary_entry, DiaryEntry)



def test_diary_entry_instantiate_invalid():
    #valid title, invalid contents
    title = "Another Title"
    contents = 54323
    with pytest.raises(Exception) as e:
        diary_entry = DiaryEntry(title, contents)
    error_message = str(e.value)
    assert error_message == "Error - title and contents must be str values."

    #invalid title, invalid contents
    title = True
    contents = "tomorrow and tomorrow and tomorrow ..."
    with pytest.raises(Exception) as e:
        diary_entry = DiaryEntry(title, contents)
    error_message = str(e.value)
    assert error_message == "Error - title and contents must be str values."

    #invalid title, invalid contents
    title = True
    contents = None
    with pytest.raises(Exception) as e:
        diary_entry = DiaryEntry(title, contents)
    error_message = str(e.value)
    assert error_message == "Error - title and contents must be str values."

#format
def test_diary_entry_format_verbatim_return():
    title = "My Title"
    contents = "These are the contents"
    diary_entry = DiaryEntry(title, contents)
    result = diary_entry.format()
    assert result == "My Title: These are the contents"

def test_diary_entry_format_different_return():
    title = "A different title entirely"
    contents = "So today I found a bear in my washing machine, like a full on polar bear. She was NOT happy."
    diary_entry = DiaryEntry(title, contents)
    result = diary_entry.format()
    assert result == "A different title entirely: So today I found a bear in my washing machine, like a full on polar bear. She was NOT happy."

#count_words
def test_diary_entry_count_words_5_words():
    title = "I'm so old..."
    contents = "Today is my 5th birthday!"
    diary_entry = DiaryEntry(title, contents)
    result = diary_entry.count_words()
    assert result == 5

def test_diary_entry_count_words_10_words():
    title = "I'm so old..."
    contents = "Today is my 5th birthday! And I already fear death."
    diary_entry = DiaryEntry(title, contents)
    result = diary_entry.count_words()
    assert result == 10

def test_diary_entry_count_words_0_words():
    title = "Nothing happened today"
    contents = ""
    diary_entry = DiaryEntry(title, contents)
    result = diary_entry.count_words()
    assert result == 0

#reading_time
def test_diary_entry_reading_time_valid_wpm_1():
    title = "Title"
    contents = ". . . . . . . . . 10"
    words_per_minute = 10
    diary_entry = DiaryEntry(title, contents)
    result = diary_entry.reading_time(words_per_minute)
    assert result == 1

def test_diary_entry_reading_time_valid_wpm_100():
    title = "Title"
    contents = ". . . . . . . . . 10"
    words_per_minute = 100
    diary_entry = DiaryEntry(title, contents)
    result = diary_entry.reading_time(words_per_minute)
    assert result == 0.1

def test_diary_entry_reading_time_invalid_wpm_0():
    title = "Title"
    contents = ". . . . . . . . . 10"
    words_per_minute = 0
    diary_entry = DiaryEntry(title, contents)
    with pytest.raises(Exception) as e:
        result = diary_entry.reading_time(words_per_minute)
    error_message = str(e.value)
    assert error_message == "Words per minute must be greater than 0."

def test_diary_entry_reading_time_invald_non_int():
    title = "Title"
    contents = ". . . . . . . . . 10"
    words_per_minute = "Cake"
    diary_entry = DiaryEntry(title, contents)
    with pytest.raises(Exception) as e:
        result = diary_entry.reading_time(words_per_minute)
    error_message = str(e.value)
    assert error_message == "Words per minute must be an int."

def test_diary_entry_reading_time_invalid_negative_int():
    title = "Title"
    contents = ". . . . . . . . . 10"
    words_per_minute = -5
    diary_entry = DiaryEntry(title, contents)
    with pytest.raises(Exception) as e:
        result = diary_entry.reading_time(words_per_minute)
    error_message = str(e.value)
    assert error_message == "Words per minute must be greater than 0."


#reading_chunk
def test_diary_entry_reading_chunk_valid_contents_1_wpm_1_minutes_1():
    title = "Title"
    contents = "Contents"
    words_per_minute = 1
    minutes = 1
    diary_entry = DiaryEntry(title, contents)
    result = diary_entry.reading_chunk(words_per_minute, minutes)
    assert result == "Contents"
    result = diary_entry.reading_chunk(words_per_minute, minutes)
    assert result == "Contents"

def test_diary_entry_reading_chunk_valid_contents_2_wpm_1_minutes_1():
    title = "Title"
    contents = "Contents beyond"
    words_per_minute = 1
    minutes = 1
    diary_entry = DiaryEntry(title, contents)
    result = diary_entry.reading_chunk(words_per_minute, minutes)
    assert result == "Contents"
    result = diary_entry.reading_chunk(words_per_minute, minutes)
    assert result == "beyond"
    result = diary_entry.reading_chunk(words_per_minute, minutes)
    assert result == "Contents"

def test_diary_entry_reading_chunk_valid_contents_10_wpm_2_minutes_2():
    title = "Title"
    contents = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10."
    words_per_minute = 2
    minutes = 1
    diary_entry = DiaryEntry(title, contents)
    result = diary_entry.reading_chunk(words_per_minute, minutes)
    assert result == "1, 2,"
    result = diary_entry.reading_chunk(words_per_minute, minutes)
    assert result == "3, 4,"
    result = diary_entry.reading_chunk(words_per_minute, minutes)
    assert result == "5, 6,"
    result = diary_entry.reading_chunk(words_per_minute, minutes)
    assert result == "7, 8,"
    result = diary_entry.reading_chunk(words_per_minute, minutes)
    assert result == "9, 10."
    result = diary_entry.reading_chunk(words_per_minute, minutes)
    assert result == "1, 2,"

def test_diary_entry_reading_chunk_valid_contents_0_wpm_1_minutes_1():
    title = "Title"
    contents = ""
    words_per_minute = 1
    minutes = 1
    diary_entry = DiaryEntry(title, contents)
    result = diary_entry.reading_chunk(words_per_minute, minutes)
    assert result == ""

def test_diary_entry_reading_chunk_invalid_wpm_0():
    title = "Title"
    contents = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10."
    words_per_minute = 0
    minutes = 1
    diary_entry = DiaryEntry(title, contents)
    with pytest.raises(Exception) as e:
        result = diary_entry.reading_chunk(words_per_minute, minutes)
    error_message = str(e.value)
    assert error_message == "Words per minute and minutes must be greater than 0."

def test_diary_entry_reading_chunk_invalid_minutes_0():
    title = "Title"
    contents = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10."
    words_per_minute = 1
    minutes = 0
    diary_entry = DiaryEntry(title, contents)
    with pytest.raises(Exception) as e:
        result = diary_entry.reading_chunk(words_per_minute, minutes)
    error_message = str(e.value)
    assert error_message == "Words per minute and minutes must be greater than 0."

def test_diary_entry_reading_chunk_invalid_non_int_values():
    title = "Title"
    contents = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10."

    #wpm and minutes both non integers
    words_per_minute = False
    minutes = None
    diary_entry = DiaryEntry(title, contents)
    with pytest.raises(Exception) as e:
        result = diary_entry.reading_chunk(words_per_minute, minutes)
    error_message = str(e.value)
    assert error_message == "Words per minute and minutes must both be integers."

    #wpm non integer
    words_per_minute = "string"
    minutes = 10
    diary_entry = DiaryEntry(title, contents)
    with pytest.raises(Exception) as e:
        result = diary_entry.reading_chunk(words_per_minute, minutes)
    error_message = str(e.value)
    assert error_message == "Words per minute and minutes must both be integers."

    #minutes non integer
    words_per_minute = 5
    minutes = None
    diary_entry = DiaryEntry(title, contents)
    with pytest.raises(Exception) as e:
        result = diary_entry.reading_chunk(words_per_minute, minutes)
    error_message = str(e.value)
    assert error_message == "Words per minute and minutes must both be integers."