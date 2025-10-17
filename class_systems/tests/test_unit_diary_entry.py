from lib.diary_entry import DiaryEntry
import pytest
"""
When given a valid title and contents, the diary_entry is instantiated
"""
def test_de_init_valid():
    de = DiaryEntry("Title", "Contents and stuff")
    assert isinstance(de, DiaryEntry)

def test_de_init_empty_string_invalid():
    #empty title
    with pytest.raises(Exception) as e:
        de = DiaryEntry("", "Contents")  
    error_message = str(e.value)
    assert error_message == "Title and contents cannot be an empty string."

    #empty contents
    with pytest.raises(Exception) as e:
        de = DiaryEntry("Title", "")  
    error_message = str(e.value)
    assert error_message == "Title and contents cannot be an empty string."

    #empty both
    with pytest.raises(Exception) as e:
        de = DiaryEntry("", "")  
    error_message = str(e.value)
    assert error_message == "Title and contents cannot be an empty string."

def test_de_init_non_string_invalid():
    #non string title
    with pytest.raises(Exception) as e:
        de = DiaryEntry(1, "Contents")  
    error_message = str(e.value)
    assert error_message == "Title and contents must be a string value."


    #non string contents
    with pytest.raises(Exception) as e:
        de = DiaryEntry("Title", None)  
    error_message = str(e.value)
    assert error_message == "Title and contents must be a string value."


    #non string both
    with pytest.raises(Exception) as e:
        de = DiaryEntry(True, 4.3241)  
    error_message = str(e.value)
    assert error_message == "Title and contents must be a string value."

def test_de_count_words_10_words():
    de = DiaryEntry("Title", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10.")
    result = de.count_words()
    assert result == 10

def test_de_reading_time_valid_wpm_above_0():
    de = DiaryEntry("Title", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10.")
    wpm = 10
    result = de.reading_time(wpm)
    assert result == 1
    wpm = 5
    result = de.reading_time(wpm)
    assert result == 2
    wpm = 1
    result = de.reading_time(wpm)
    assert result == 10

def test_de_reading_time_invalid_wpm_below_1():
    de = DiaryEntry("Title", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10.")
    wpm = 0
    with pytest.raises(Exception) as e:
        result = de.reading_time(wpm)
    error_message = str(e.value)
    assert error_message == "Wpm must be greater than 0."

    wpm = -1
    with pytest.raises(Exception) as e:
        result = de.reading_time(wpm)
    error_message = str(e.value)
    assert error_message == "Wpm must be greater than 0."

def test_de_reading_time_invalid_non_int():
    de = DiaryEntry("Title", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10.")
    wpm = "Couch potato"
    with pytest.raises(Exception) as e:
        result = de.reading_time(wpm)
    error_message = str(e.value)
    assert error_message == "Wpm must be an integer."

    wpm = False
    with pytest.raises(Exception) as e:
        result = de.reading_time(wpm)
    error_message = str(e.value)
    assert error_message == "Wpm must be an integer."

    wpm = 3.532
    with pytest.raises(Exception) as e:
        result = de.reading_time(wpm)
    error_message = str(e.value)
    assert error_message == "Wpm must be an integer."

def test_de_reading_chunk_valid_returns_chunk_and_loops():
    de = DiaryEntry("Title", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10.")
    wpm = 2
    minutes = 1
    result = de.reading_chunk(wpm, minutes)
    assert result == "1, 2,"
    
    result = de.reading_chunk(wpm, minutes)
    assert result == "3, 4,"

    result = de.reading_chunk(wpm, minutes)
    assert result == "5, 6,"

    result = de.reading_chunk(wpm, minutes)
    assert result == "7, 8,"

    result = de.reading_chunk(wpm, minutes)
    assert result == "9, 10."

    result = de.reading_chunk(wpm, minutes)
    assert result == "1, 2,"

def test_de_reading_chunk_invalid_parameters_under_0():
    de = DiaryEntry("Title", "Contents")
    
    #wpm < 1
    wpm = 0
    minutes = 1
    with pytest.raises(Exception) as e:
        de.reading_chunk(wpm, minutes)
    error_message = str(e.value)
    assert error_message == "Wpm and minutes must be greater than 0."

    #minutes < 1
    wpm = 1
    minutes = 0
    with pytest.raises(Exception) as e:
        de.reading_chunk(wpm, minutes)
    error_message = str(e.value)
    assert error_message == "Wpm and minutes must be greater than 0."

    #both < 1
    wpm = 0
    minutes = 0
    with pytest.raises(Exception) as e:
        de.reading_chunk(wpm, minutes)
    error_message = str(e.value)
    assert error_message == "Wpm and minutes must be greater than 0."

def test_de_reading_chunk_invalid_parameters_non_int():
    de = DiaryEntry("Title", "Contents")
    
    #wpm non int
    wpm = "Farty"
    minutes = 1
    with pytest.raises(Exception) as e:
        de.reading_chunk(wpm, minutes)
    error_message = str(e.value)
    assert error_message == "Wpm and minutes must be an integer."
    

    #minutes non int
    wpm = 1
    minutes = False
    with pytest.raises(Exception) as e:
        de.reading_chunk(wpm, minutes)
    error_message = str(e.value)
    assert error_message == "Wpm and minutes must be an integer."
    

    #both non int
    wpm = None
    minutes = 45.15321
    with pytest.raises(Exception) as e:
        de.reading_chunk(wpm, minutes)
    error_message = str(e.value)
    assert error_message == "Wpm and minutes must be an integer."