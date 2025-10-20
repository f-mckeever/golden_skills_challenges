from lib.todo_list import *
"""
Test TodoList instantiates
"""

def test_todolist_instantiates():
    tl = TodoList()
    assert isinstance(tl, TodoList)