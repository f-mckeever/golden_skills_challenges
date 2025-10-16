from lib.task_manager import *
import pytest

"""
Given a new task, the task will be added to the task list
"""
def test_tm_given_task_task_added_to_tasks():
    tm = TaskManager()
    task = "Buy milk"
    tm.add_task(task)
    assert task in tm.get_tasks()

"""
Given an empty string to add as a task, the program throws an exception. "Task cannot be an empty string."
"""
def test_tm_given_empty_str_add_task_raises_exception():
    tm = TaskManager()
    task = ""
    with pytest.raises(Exception) as e:
        tm.add_task(task)
    error_message = str(e.value)
    assert error_message == "Task cannot be an empty string."

"""
Given a non string value to add as a task, the program throws an exception. "Task must be a string value."
"""
def test_tm_given_non_string_add_task_raises_exception():
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
def test_tm_no_tasks_add_task_raises_exception():
    tm = TaskManager()
    with pytest.raises(Exception) as e:
        result = tm.show_tasks()
    error_message = str(e.value)
    assert error_message == "No tasks to complete."

"""
Given tasks have been added
#show_tasks returns "You need to:" + each task
"""
def test_tm_show_tasks_returns_tasks():
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
def test_tm_give_no_tasks_complete_task_raise_exception():
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
def test_tm_given_task_no_match_complete_task_raises_exception():
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
def test_tm_complete_task_non_string_raises_exception():
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

def test_tm_complete_task_valid_string_removes_task():
    tm = TaskManager()
    tm.add_task("Hire a lawyer")
    tm.add_task("Create an alibi")
    tm.add_task("Intimidate witnesses")
    starting_list = ['Hire a lawyer', 'Create an alibi', 'Intimidate witnesses']
    assert starting_list == tm.get_tasks()

    tm.add_task("Come clean")
    assert starting_list != tm.get_tasks()
    assert tm.get_tasks()[-1] == "Come clean"

    tm.complete_task("Come clean")
    assert starting_list == tm.get_tasks()
    assert "Come clean" not in tm.get_tasks()
