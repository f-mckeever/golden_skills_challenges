from lib.diary_entry import *
from lib.task_list import *
from lib.contact_list import *
from lib.contact import *
from lib.task import *

class Diary():
    #init
    #parameters -> none
    #returns -> none
    #sides -> initialise empty lists:   entries_list = []
                                        # tasks_list = TaskList()
                                        # contact_list = []  
    def __init__(self):
        self.entry_list = []
        self.task_list = TaskList()
        self.contact_list = ContactList()

    #add_entry
    #parameters -> entry : DiaryEntry
    #returns -> none
    #sides -> appends entry to entries_list
    def add_entry(self, entry):
        if type(entry) == DiaryEntry:
            self.entry_list.append(entry)
        else:
            raise Exception("Entry must be an instance of DiaryEntry.")

    #entries
    #parameters -> none
    #returns -> all entries from entries_list
    #sides -> none
    def entries(self):
        if len(self.entry_list) > 0:
            return self.entry_list
        else:
            raise Exception("Entry list is currently empty.")

    #best_entry
    #parameters -> wpm: int
    #           -> minutes: int
    #returns -> entry that is closest in time to read, without going over
    #sides -> none
    def best_entry(self, wpm, minutes):
        if len(self.entries()) > 0:
            if type(wpm) == int and type(minutes) ==int:
                if wpm > 0 and minutes > 0:
                    upper_minute_limit = minutes
                    print(upper_minute_limit)
                    
                    current_highest_reading_time = self.entries()[0].reading_time(wpm)

                    to_return = "No entry found matching reading specifications."

                    #loop every entry
                    for entry in self.entries():


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

    #tasks
    #parameters -> none
    #returns -> list of tasks, and whether they have been completed or not
    #sides -> none
    def tasks(self):
        return self.task_list.get_tasks()

    #contacts
    #parameters -> none
    #returns -> list of contacts
    #sides -> none
    def contacts(self):
        return self.contact_list.get_contact_list()

    #update_contacts
    #params -> list of diary entries: List
    #returns -> none
    #sides -> creates new Contact for each phone number found in diary entries, and appends them to self.contact_list
    def update_contacts(self):
        
        #loop over each entry
        for entry in self.entry_list:
            #loop over words in entry
                

                for word in entry.contents.split(" "):
                    
                #if word matches structure of +44 then 10 numbers then that's a number
                    if word[0:3] == "+44" and len(word) == 13 and word[1:].isnumeric():
                    #capture the word at the index before as the name
                        number = word
                        name = entry.contents.split(" ")[entry.contents.split(" ").index(word) - 1]
                        #create new Contact instance and append it to the ContactList
                        contact = Contact(name, number)
                        self.contact_list.add(contact)
