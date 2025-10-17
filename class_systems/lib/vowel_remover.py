# File: lib/vowel_remover.py

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        vowelless_text = ""
        while i < len(self.text):
            if self.text[i].lower() not in self.vowels:
                vowelless_text += self.text[i]
            i += 1
        return vowelless_text

vr = VowelRemover("aeiou")
result = vr.remove_vowels()
print(result)