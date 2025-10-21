class Task():
    #init
    #params -> task: str
    #returns -> none
    #sides -> instantiate self
    def __init__(self, task):
        if type(task) == str:
            if len(task.strip()) > 0:
                self.task = task
                self.complete = False
            else:
                raise Exception("Task cannot be an empty string.")
        else:
            raise Exception("Task must be a string.")

    #get_task
    #params -> none
    #returns -> task
    #sides -> none
    def get_task(self):
        return self.task

    #mark_complete
    #params -> none
    #returns -> none
    #sides -> set self.complete to True
    def mark_complete(self):
        self.complete = True

    #mark_incomplete
    #params -> none
    #returns -> none
    #sides -> set self.complete to False
    def mark_incomplete(self):
        self.complete = False

