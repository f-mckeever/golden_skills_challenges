from lib.task import *

class TaskList():
    #init
    #params -> none
    #returns -> none
    #sides -> instantiates self, self.task_list = []
    def __init__(self):
        self.task_list = []

    #add
    #params -> task : Task
    #returns -> none
    #sides -> appends task to task_list
    def add(self, task):
        if isinstance(task, Task):
            self.task_list.append(task)
        else:
            raise Exception("Task must be an instance of Task.")
    
    #get_tasks
    #params -> none
    #returns -> self.task_list
    #sides -> none
    def get_tasks(self):
        if len(self.task_list) > 0:
            return self.task_list
        else:
            raise Exception("Task list is currently empty.")

    #complete_all
    #params -> none
    #returns -> none
    #sides -> set all tasks in task_list to complete
    def complete_all(self):
        if len(self.task_list) > 0:
            for task in self.task_list:
                task.mark_complete()
        else:
            raise Exception("Task list is currently empty.")

    #incomplete_all
    #params -> none
    #returns -> none
    #sides -> set all tasks in task_list to incomplete
    def incomplete_all(self):
        if len(self.task_list) > 0:
            for task in self.task_list:
                task.mark_incomplete()
        else:
            raise Exception("Task list is currently empty.")


