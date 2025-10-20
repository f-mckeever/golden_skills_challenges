# File: lib/todo_list.py
from lib.todo import *

class TodoList:
    def __init__(self):
        self.todo_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        if type(todo) == Todo:
            self.todo_list.append(todo)
        else:
            raise Exception("Todo must be an instance of Todo.")

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_list = [todo for todo in self.todo_list if todo.complete == False]
        if len(incomplete_list) > 0:
            return incomplete_list
        else:
            raise Exception("No incomplete tasks found.")

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_list = [todo for todo in self.todo_list if todo.complete == True]
        if len(complete_list) > 0:
            return complete_list
        else:
            raise Exception("No complete tasks found.")
        

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self.todo_list:
            todo.mark_complete()
        