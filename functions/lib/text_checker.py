def text_checker(text):
    if len(text) > 2:
        return text_starts_with_capital(text) and text_ends_punctuation(text)
    raise Exception("Text is too short to check.")

def text_starts_with_capital(text):
    return text[0].isupper()

def text_ends_punctuation(text):
    required_symbols = ".?!"
    return text[-1] in required_symbols