from task.task_model import TaskModel
from core.utils.create_error import create_error
from playhouse.shortcuts import model_to_dict


def create_task(name):
    try:
        task = TaskModel.create(name=name)
        task.save()

        return None, model_to_dict(task)
    except NameError:
        return create_error(500, NameError), None


def get_tasks():
    try:
        tasks = TaskModel.select()

        tasks_list = list(tasks.dicts())

        return None, tasks_list
    except NameError:
        return create_error(500, NameError), None





