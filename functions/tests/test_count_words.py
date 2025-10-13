from lib.count_words import *
#Takes a string as an input, returns the number of words in that string
#Empty string will return 0

#String of 1 word will return 1

#String of X words will return X

def test_count_words_empty_string():
    string = ""
    result = count_words(string)
    assert result == 0

def test_count_words_one_word_string_returns_one():
    string = "tool"
    result = count_words(string)
    assert result == 1

def test_count_words_many_words():
    string = "i just started listening to tool again there and i cant lie, they're really quite groovy, the drumming and rhythm is immaculate and so intricate it really gives me a new found appreciation for them as a band, even before i jabber on about the soundscapes and immersive songs"
    result = count_words(string)
    assert result == 49