from lib.task import *
import pytest
"""
Given a valid task, #get_task returns the task, marked as incomplete
"""

def test_task_valid_params_get_task():
    task = Task("Listen to the new podcast.")
    assert task.get_task() == "Listen to the new podcast."
    assert task.complete == False

"""
Given an empty string, raise exception
"""
def test_task_invalid_params_empty_string():
    with pytest.raises(Exception) as e:
        task = Task("")
    err_msg = str(e.value)
    assert err_msg == "Task cannot be an empty string."
    
"""
Given a non  string, raise exception
"""
def test_task_invalid_params_empty_string():
    with pytest.raises(Exception) as e:
        task = Task(67)
    err_msg = str(e.value)
    assert err_msg == "Task must be a string."

"""
Given a valid string, #mark_complete sets task.complete to True
"""
def test_task_complete_sets_true():
    task = Task("Just put the ball in the net.")
    assert task.complete == False

    task.mark_complete()

    assert task.complete == True



"""
Given a valid string, #mark_incomplete sets task.complete to True
"""
def test_task_incomplete_sets_false():
    task = Task("Just put the ball in the net.")
    assert task.complete == False

    task.mark_complete()
    assert task.complete == True


    task.mark_incomplete()
    assert task.complete == False