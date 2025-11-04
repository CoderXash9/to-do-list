"""TodoList module for managing tasks."""

import json
import os
from typing import List, Optional
from .task import Task


class TodoList:
    """Manages a collection of tasks."""

    def __init__(self, data_dir: str = "data"):
        """Initialize the TodoList.

        Args:
            data_dir: Directory where tasks are stored
        """
        self.data_dir = data_dir
        self.tasks_file = os.path.join(data_dir, "tasks.json")
        self.tasks: List[Task] = []
        self._ensure_data_dir()
        self._load_tasks()

    def _ensure_data_dir(self) -> None:
        """Ensure the data directory exists."""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def _load_tasks(self) -> None:
        """Load tasks from the JSON file."""
        if os.path.exists(self.tasks_file):
            with open(self.tasks_file, "r") as f:
                data = json.load(f)
                self.tasks = [
                    Task(
                        title=task["title"],
                        description=task.get("description", ""),
                        task_id=task.get("id"),
                    )
                    for task in data
                ]

    def _save_tasks(self) -> None:
        """Save tasks to the JSON file."""
        with open(self.tasks_file, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=2)

    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task.

        Args:
            title: Task title
            description: Task description

        Returns:
            The created task
        """
        task_id = max([t.id for t in self.tasks], default=0) + 1
        task = Task(title=title, description=description, task_id=task_id)
        self.tasks.append(task)
        self._save_tasks()
        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if successful, False otherwise
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                self._save_tasks()
                return True
        return False

    def complete_task(self, task_id: int) -> bool:
        """Mark a task as complete.

        Args:
            task_id: ID of the task to complete

        Returns:
            True if successful, False otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete()
                self._save_tasks()
                return True
        return False

    def get_all_tasks(self) -> List[dict]:
        """Get all tasks.

        Returns:
            List of task dictionaries
        """
        return [task.to_dict() for task in self.tasks]

    def get_pending_tasks(self) -> List[dict]:
        """Get all pending (incomplete) tasks.

        Returns:
            List of pending task dictionaries
        """
        return [task.to_dict() for task in self.tasks if not task.completed]

    def get_completed_tasks(self) -> List[dict]:
        """Get all completed tasks.

        Returns:
            List of completed task dictionaries
        """
        return [task.to_dict() for task in self.tasks if task.completed]
