class Contact():
    #init
    #params -> name: str "", number: str
    #returns -> none
    # sides -> none
    def __init__(self, name, number):
        if type(name) == str and type(number) == str:
            if len(name) > 0 and len(number) > 0:
                self.name = name
                self.number = number
            else:
                raise Exception("Name and number cannot be empty strings.")
        else:
            raise Exception("Name and number must be strings.")

    #get_contact
    #params -> none
    #returns -> str: f"{name}, {number}"
    def get_contact(self):
        return f"{self.name}, {self.number}"