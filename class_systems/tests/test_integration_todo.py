from lib.todo import *
from lib.todo_list import *
import pytest

"""
Given a list of todos, #incomplete returns a list of incomplete todos
"""

def test_tl_incomplete_returns_list():
    tl = TodoList()
    td1 = Todo("Relax.")
    td2 = Todo("Turn on the radio.")
    td3 = Todo("Pry open your third eye.")
    tl.add(td1)
    tl.add(td2)
    tl.add(td3)
    
    result = tl.incomplete()
    assert result == [td1, td2, td3]

"""
Given a list of todos, when some are marked as complete, #complete returns a
list of the complete todos
"""

def test_todolist_complete_returns_complete_todos():
    tl = TodoList()
    td1 = Todo("Relax.")
    td2 = Todo("Turn on the radio.")
    td3 = Todo("Pry open your third eye.")
    tl.add(td1)
    tl.add(td2)
    tl.add(td3)

    tl.todo_list[0].mark_complete()
    tl.todo_list[2].mark_complete()
    
    result = tl.complete()
    assert result == [td1, td3]

"""
Given a non Todo, #add raises exception
"""

def test_todolist_add_invalid_non_todo():
    tl = TodoList()
    td = "Tool"
    with pytest.raises(Exception) as e:
        tl.add(td)
    err_message = str(e.value)
    assert err_message == "Todo must be an instance of Todo."

"""
Given no todos are incomplete, #incomplete raises exception
"""
def test_todolist_incomplete_empty_list():
    tl = TodoList()
    with pytest.raises(Exception) as e:
        tl.incomplete()
    err_mess = str(e.value)
    assert err_mess == "No incomplete tasks found."

"""
Given no todos are complete, #complete raises exception
"""
def test_todolist_complete_empty_list():
    tl = TodoList()
    with pytest.raises(Exception) as e:
        tl.complete()
    err_mess = str(e.value)
    assert err_mess == "No complete tasks found."


"""
Given tasks have been added, #give_up marks all tasks as complete
"""

def test_todolist_giveup_valid():
    tl = TodoList()
    td1 = Todo("Kick drum.")
    td2 = Todo("Snare.")
    td3 = Todo("Crash.")

    tl.add(td1)
    tl.add(td2)
    tl.add(td3)

    initial_todo_list = tl.incomplete()
    assert initial_todo_list == [td1, td2, td3]

    tl.give_up()

    end_todo_list = tl.complete()
    assert end_todo_list == [td1, td2, td3]

    with pytest.raises(Exception) as e:
        end_incomplete_list = tl.incomplete()
    err_msg = str(e.value)
    assert err_msg == "No incomplete tasks found."