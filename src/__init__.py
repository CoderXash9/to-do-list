"""To-Do List Application Package

A Python-based To-Do List application with a user-friendly interface.
Manage your tasks efficiently with features like adding, editing, deleting,
and marking tasks as complete.
"""

__version__ = "1.0.0"
__author__ = "Ashwini Purohit"
__email__ = "codexash9@example.com"

from .task import Task
from .todo_list import TodoList

__all__ = ["Task", "TodoList"]
