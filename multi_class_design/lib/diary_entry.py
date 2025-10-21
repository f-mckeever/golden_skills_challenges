
class DiaryEntry():
    #init
    #params -> title: str, contents: str
    #returns -> none
    #sides -> instantiates self
    def __init__(self, title, contents):
        if type(title) == str and type(contents) == str:
            if len(title) > 0 and len(contents) > 0:
                self.title = title
                self.contents = contents
            else:
                raise Exception("Title and contents must not be empty strings.")
        else:
            raise Exception("Title and contents must be strings.")

    #get_title
    #params -> none
    #returns -> self.title
    #sides -> none
    def get_title(self):
        return self.title

    #get_contents
    #params -> none
    #returns -> self.contents
    #sides -> none
    def get_contents(self):
        return self.contents

    #count_words
    #params -> none
    #returns -> number of words in contents
    #sides -> none  
    def count_words(self):
        words = self.contents.split(" ")
        return len(words)

    #reading_time
    #params -> words: int, wpm: int
    #returns -> int: time to read entry in minutes
    #sides -> none
    def reading_time(self, wpm):
        if type(wpm) == int:
            if wpm > 0:
                entry_length = self.count_words()
                return int(entry_length / wpm)
            else:
                raise Exception("Wpm must be greater than 0.")
        else:
            raise Exception("Wpm must be an integer.")
