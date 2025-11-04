"""Task module for the To-Do List application."""

from datetime import datetime
from typing import Optional


class Task:
    """Represents a single task in the to-do list."""

    def __init__(
        self,
        title: str,
        description: Optional[str] = None,
        task_id: Optional[int] = None,
    ):
        """Initialize a new Task.

        Args:
            title: The task title
            description: Optional task description
            task_id: Optional task ID
        """
        self.id = task_id
        self.title = title
        self.description = description or ""
        self.completed = False
        self.created_at = datetime.now().isoformat()
        self.completed_at: Optional[str] = None

    def mark_complete(self) -> None:
        """Mark the task as complete."""
        self.completed = True
        self.completed_at = datetime.now().isoformat()

    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        self.completed = False
        self.completed_at = None

    def update(self, title: str, description: str = "") -> None:
        """Update the task details.

        Args:
            title: New task title
            description: New task description
        """
        self.title = title
        self.description = description

    def to_dict(self) -> dict:
        """Convert the task to a dictionary.

        Returns:
            Dictionary representation of the task
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at,
            "completed_at": self.completed_at,
        }

    def __str__(self) -> str:
        """Return string representation of the task."""
        status = "✓" if self.completed else "○"
        return f"{status} {self.title}"
