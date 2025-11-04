#!/usr/bin/env python3
"""Main entry point for the To-Do List application."""

import click
from todo_list import TodoList


@click.group()
def cli():
    """To-Do List Application - Manage your tasks efficiently."""
    pass


@cli.command()
@click.argument('task')
def add(task):
    """Add a new task to the to-do list."""
    todo = TodoList()
    todo.add_task(task)
    click.echo(click.style('✓ Task added successfully!', fg='green'))


@cli.command()
def list():
    """List all tasks in the to-do list."""
    todo = TodoList()
    tasks = todo.get_all_tasks()
    if not tasks:
        click.echo('No tasks found.')
    else:
        for i, task in enumerate(tasks, 1):
            status = '✓' if task['completed'] else '○'
            click.echo(f"{status} {i}. {task['title']}")


@cli.command()
@click.argument('task_id', type=int)
def complete(task_id):
    """Mark a task as complete."""
    todo = TodoList()
    todo.complete_task(task_id)
    click.echo(click.style('✓ Task marked as complete!', fg='green'))


@cli.command()
@click.argument('task_id', type=int)
def delete(task_id):
    """Delete a task from the to-do list."""
    todo = TodoList()
    todo.delete_task(task_id)
    click.echo(click.style('✓ Task deleted successfully!', fg='yellow'))


if __name__ == '__main__':
    cli()
