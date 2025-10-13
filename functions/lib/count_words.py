def count_words(string):
    if len(string) > 0:
        words = string.split(" ")
        return len(words)
    return 0