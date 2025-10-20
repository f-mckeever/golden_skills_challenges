from lib.todo import *
import pytest
"""
Given a task as a string, the todo is instantiated, and the complete
prop and task is set to task
"""
def test_todo_instantiates_valid():
    todo = Todo("Mine the diamonds.")
    assert isinstance(todo, Todo)
    assert todo.complete == False
    assert todo.task == "Mine the diamonds."

"""
Given an empty string as a task, Todo raises an exception
"""

def test_todo_invalid_empty_string_task():
    with pytest.raises(Exception) as e:
        todo = Todo("")
    err_message = str(e.value)
    assert err_message == "Task must not be an empty string."
    

"""
Given an non string as a task, Todo raises an exception
"""

def test_todo_invalid_empty_string_task():
    with pytest.raises(Exception) as e:
        todo = Todo(0)
    err_message = str(e.value)
    assert err_message == "Task must be a string."

"""
Todo #mark_complete, update todo.complete to True from initial False
"""

def test_todo_mark_complete_updates_complete_boolean():
    todo = Todo("Craft the tings.")
    assert todo.complete == False

    todo.mark_complete()
    assert todo.complete == True