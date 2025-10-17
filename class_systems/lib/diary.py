# File: lib/diary.py
from lib.diary_entry import *

class Diary:
    def __init__(self):
        self.entries_list = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        if isinstance(entry, DiaryEntry):
            self.all().append(entry)
        else:
            raise Exception("Entry must be an instance of DiaryEntry.")

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.entries_list

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        if len(self.all()) > 0:
            word_count = 0
            for entry in self.all():
                word_count += entry.count_words()
            return word_count
        else:
            raise Exception("Entries list is currently empty.")

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        if type(wpm) == int:
            if wpm > 0:
                return int(self.count_words() / wpm)
            else:
                raise Exception("Wpm must be greater than 0.")
        else:
            raise Exception("Wpm must be an integer.")

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        if len(self.all()) > 0:
            if type(wpm) == int and type(minutes) ==int:
                if wpm > 0 and minutes > 0:
                    upper_minute_limit = minutes
                    print(upper_minute_limit)
                    
                    current_highest_reading_time = self.all()[0].reading_time(wpm)

                    to_return = "No entry found matching reading specifications."

                    #loop every entry
                    for entry in self.all():


                        #if entry.reading_time() is underneath the upper bounds
                        print("Reading time = ", entry.reading_time(wpm))
                        if entry.reading_time(wpm) < upper_minute_limit:


                            #choose biggest value, that isn't over the upper bounds
                            if entry.reading_time(wpm) >= current_highest_reading_time:
                                current_highest_reading_time = entry.reading_time(wpm)
                                to_return = entry
                            
                    #return the entry with the longest contents within limit        
                    return to_return
                else:
                    raise Exception("Wpm and minutes must be greater than 0.")
            else:
                raise Exception("Wpm and minutes must be an integer.")
        else:
            raise Exception("Entries list is currently empty.")

