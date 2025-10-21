from lib.task_list import *

"""
Task list instantiate with an empty list for tasks
"""

def test_tasklist_instantiates_task_list():
    tl = TaskList()
    assert isinstance(tl, TaskList)
    assert tl.task_list == []