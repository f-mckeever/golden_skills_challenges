class DiaryEntry:
    def __init__(self, title, contents):
        if isinstance(title, str) and isinstance(contents, str):
            self.title = title
            self.contents = contents
            self.contents_list = contents.split(" ")
        else:
            raise Exception("Error - title and contents must be str values.")

    def format(self):
        return self.title + ": " + self.contents

    def count_words(self):
        if self.contents == "":
            return 0
        return len(self.contents.split(" "))

    def reading_time(self, wpm):
        if isinstance(wpm, int):
            if wpm <= 0:
                raise Exception("Words per minute must be greater than 0.")
            return len(self.contents.split(" ")) / wpm
        raise Exception("Words per minute must be an int.")

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        if isinstance(wpm, int) and isinstance(minutes, int):
            if wpm > 0 and minutes > 0:
                #words read in chunk = wpm * minutes
                words_read_in_chunk = wpm * minutes
                #chunk = self.contents.split(" ")
                words_in_contents = self.contents_list
                #return words in contents [0:words_read_in_chunk]
                chunk = " ".join(words_in_contents[0:words_read_in_chunk])

                #remove each read word in chunk from contents_list 
                counter = 0
                while counter < words_read_in_chunk :
                    self.contents_list.pop(0)
                    counter += 1
                
                #if contents_list is empty, reset it to be the self.contents.split(" ")
                if len(self.contents_list) == 0:
                    self.contents_list = self.contents.split(" ")
            else:
                raise Exception("Words per minute and minutes must be greater than 0.")
        else:
            raise Exception("Words per minute and minutes must both be integers.")
        return chunk
