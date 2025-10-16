class TaskManager():
    
    #__init__
    def __init__(self):
        #list to store user tasks
        self._tasks = []

    #adds a task to the list
    def add_task(self, task):
        if isinstance(task, str):
            if len(task) > 0:
                self.tasks.append(task)
            else:
                raise Exception("Task cannot be an empty string.")
        else:
            raise Exception("Task must be a string value.")

    #returns the tasks list
    def get_tasks(self):
        return self._tasks
    
    #returns the tasks from the list, along with a "You need to:" opening line
    def show_tasks(self):
        if len(self._tasks) > 0:
            task_string = "You need to:"
            for task in self.tasks:
                task_string += f"\n{task}"
            return task_string
        else:
            raise Exception("No tasks to complete.")

    #If task exists, it marks it as complete, removing it from the list
    def complete_task(self, task):
        if isinstance(task, str):
            if len(self._tasks) > 0:
                if task in self.tasks:
                    print(f"You successfully completed the task: {task}!")
                    self._tasks.remove(task)
                else:
                    raise Exception("No task found with that name.")
            else:
                raise Exception("Task list is currently empty.")
        else:
            raise Exception("Task must be a string value.")