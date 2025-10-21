import pytest
from lib.task import *
from lib.task_list import *

"""
When given a valid task
#get_tasks returns the task_list, with the task added to it
"""

def test_tasklist_add_task_get_tasks():
    tl = TaskList()
    assert tl.task_list == []
    t1 = Task("Destailise the opposition.")
    tl.add(t1)
    assert t1 in tl.task_list
    assert tl.get_tasks() == [t1]

"""
When given an invalid task (not instance of Task)
#add raises an exception
"""

def test_tasklist_add_invalid_non_task_param():
    tl = TaskList()
    with pytest.raises(Exception) as e:
        tl.add("fart")
    err_msg = str(e.value)
    assert err_msg == "Task must be an instance of Task."

"""
When task_list is empty
#get_tasks() raises exception
#complete_all() raises exception
#incomplete_all() raises exception
"""

def test_tasklist_get_tasks_empty_list_raises_exception():
    tl = TaskList()

    with pytest.raises(Exception) as e:
        tl.get_tasks()
    err_msg = str(e.value)
    assert err_msg == "Task list is currently empty."

    with pytest.raises(Exception) as e:
        tl.complete_all()
    err_msg = str(e.value)
    assert err_msg == "Task list is currently empty."

    with pytest.raises(Exception) as e:
        tl.incomplete_all()
    err_msg = str(e.value)
    assert err_msg == "Task list is currently empty."

"""
When task_list is not empty
#complete_all sets all tasks to complete (True)
"""

def test_tasklist_complete_all_sets_all_complete_to_true():
    tl = TaskList()
    t1 = Task("Predict the score.")
    t2 = Task("Please don't say 0-0.")
    t3 = Task("Please don't say 0-0 again.")

    tl.add(t1)
    tl.add(t2)
    tl.add(t3)

    assert t1.complete == False
    assert t2.complete == False
    assert t3.complete == False

    tl.complete_all()

    assert t1.complete == True
    assert t2.complete == True
    assert t3.complete == True

"""
When task_list is not empty
#complete_all sets all tasks to complete (True)
"""

def test_tasklist_complete_all_sets_all_complete_to_true():
    tl = TaskList()
    t1 = Task("Predict the score.")
    t2 = Task("Please don't say 0-0.")
    t3 = Task("Please don't say 0-0 again.")

    tl.add(t1)
    tl.add(t2)
    tl.add(t3)

    assert t1.complete == False
    assert t2.complete == False
    assert t3.complete == False

    tl.complete_all()

    assert t1.complete == True
    assert t2.complete == True
    assert t3.complete == True

    tl.incomplete_all()

    assert t1.complete == False
    assert t2.complete == False
    assert t3.complete == False