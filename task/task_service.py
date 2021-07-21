from task.task_model import Task
from core.utils.create_error import create_error
from playhouse.shortcuts import model_to_dict


def create_task(name):
    try:
        task = Task.create(name=name)
        task.save()

        return None, model_to_dict(task)
    except NameError:
        return create_error(500, NameError), None


def get_tasks():
    try:
        tasks = Task.select()

        tasks_list = list(tasks.dicts())

        return None, tasks_list
    except NameError:
        return create_error(500, NameError), None





