# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

"""
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.
"""

User wants a program to manage their tasks -> TaskManager

Keep track of tasks -> store tasks in a LIST

Tasks would be descriptive -> tasks should be STRINGS

Can add tasks -> append tasks to the LIST

Can see a list of tasks -> PRINT all tasks to terminal

Can mark tasks as complete -> remove/pop them from LIST



## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TaskManager():

    def __init__(self):
        #Parameters:
        #   none
        #Side effects:
        #   Sets the tasks property of the self object to an empty list
        pass

    def get_tasks(self):
        #Parameters:
        #   None
        #Returns:
        #   the contents of tasks
        pass



    def add_task(self, task):
        #Parameters:
        #   task: string representing a single task
        #Returns:
        #   Nothing
        #Side-effects:
        #   Appends the task self.tasks
        #   Throws an exception if empty string is provided
        #   Throws an exception if a non-string is provided
        pass


    def show_tasks(self):
        #Parameters:
        #   None
        #Returns:
        #   A string containing "You need to:" plus each task in self.tasks on new line OR "No tasks to complete."
        pass

    def complete_task(self, task):
        #Parameters:
        #   Task
        #Returns:
        #   String reflecting which task the user has completed
        #Side-effects:
        #   Removes the completed task from self.tasks
        #   Raises exception if task list is empty: "Task list is currently empty."
        #   Raises exception if no task matching that name is found: "No task found with that name."
        pass


```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a new task, the task will be added to the task list
"""
tm = TaskManager()
task = "Buy milk"
tm.add_task(task)
assert task in tm.get_tasks()

"""
Given an empty string to add as a task, the program throws an exception. "Task cannot be an empty string."
"""
tm = TaskManager()
task = ""
with pytest.raises(Exception) as e:
    tm.add_task(task)
error_message = str(e.value)
assert error_message == "Task cannot be an empty string."

"""
Given a non string value to add as a task, the program throws an exception. "Task must be a string value."
"""
tm = TaskManager()
task = 5
with pytest.raises(Exception) as e:
    tm.add_task(task)
error_message = str(e.value)
assert error_message == "Task must be a string value."

task = False
with pytest.raises(Exception) as e:
    tm.add_task(task)
error_message = str(e.value)
assert error_message == "Task must be a string value."

task = None
with pytest.raises(Exception) as e:
    tm.add_task(task)
error_message = str(e.value)
assert error_message == "Task must be a string value."

"""
Given no tasks have been added 
#show_tasks returns "No tasks to complete."
"""

tm = TaskManager()
result = tm.show_tasks()
assert result == "No tasks to complete."


"""
Given tasks have been added
#show_tasks returns "You need to:" + each task
"""
tm = TaskManager()
task1 = "Buy milk"
tm.add_task(task1)
result = tm.show_tasks()
assert result == "You need to:\nBuy milk"

task2 = "Hoover the stairs"
tm.add_task(task2)
result = tm.show_tasks()
assert result == "You need to:\nBuy milk\nHoover the stairs"

"""
Given no tasks have been added
#complete_task raises an exception "Task list is currently empty."

"""
tm = TaskManager()
task_to_complete = "Bury the hatchet"
with pytest.raises(Exception) as e:
    tm.complete_task(task_to_complete)
error_message = str(e.value)
assert error_message == "Task list is currently empty."

"""
Given tasks have been added but no task matching the given name exists in it
#complete_task raises an exception "No task found with that name."

"""
tm = TaskManager()
task = "Hide the evidence"
tm.add_task(task)
task_to_complete = "Bury the hatchet"
with pytest.raises(Exception) as e:
    tm.complete_task(task_to_complete)
error_message = str(e.value)
assert error_message == "No task found with that name."

"""
Given a non string value
#complete_task raises an Exception "Task must be a string value."
"""
tm = TaskManager()
task = "Hide the evidence"
tm.add_task(task)
task_to_complete = 0
with pytest.raises(Exception) as e:
    tm.complete_task(task_to_complete)
error_message = str(e.value)
assert error_message == "Task must be a string value."

"""
Given a valid task
#complete_task removes the task from the task list
"""

tm = TaskManager()
tm.add_task("Hire a lawyer")
tm.add_task("Create an alibi")
tm.add_task("Intimidate witnesses")

starting_list = tm.get_tasks()

tm.add_task("Come clean")
tm.complete_task("Come clean")

end_list = tm.get_tasks()

assert starting_list == end_list
```
_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
