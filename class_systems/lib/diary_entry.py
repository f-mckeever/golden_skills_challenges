# File: lib/diary_entry.py

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        if type(title) == str and type(contents) == str:
            if len(title) > 0 and len(contents) > 0:
                self.title = title
                self.contents = contents
                self.unread_words = self.contents.split(" ")
            else:
                raise Exception("Title and contents cannot be an empty string.")
        else:
            raise Exception("Title and contents must be a string value.")

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        return len(self.contents.split(" "))

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        if type(wpm) == int:
            if wpm > 0:
                return (int(len(self.contents.split(" ")) / wpm ))
            else:
                raise Exception("Wpm must be greater than 0.")
        else:
            raise Exception("Wpm must be an integer.")

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        if type(wpm) == int and type(minutes) == int:
            if wpm > 0 and minutes > 0:
                words_to_read_in_chunk = wpm * minutes

                if len(self.unread_words) == 0:
                    self.unread_words = self.contents.split(" ")

                chunk_to_return = " ".join(self.unread_words[0:words_to_read_in_chunk])
                self.unread_words = self.unread_words[words_to_read_in_chunk:]

                return chunk_to_return
            else:
                raise Exception("Wpm and minutes must be greater than 0.")
        else:
            raise Exception("Wpm and minutes must be an integer.")


