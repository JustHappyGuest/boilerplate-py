from playhouse.shortcuts import model_to_dict

from task.task_model import TaskModel
from core.utils.create_error import create_error


def create_task(current_user, name):
    try:
        task = TaskModel.create(user_id=current_user.id, name=name)
        task.save()


        return None, model_to_dict(task)
    except NameError:
        return create_error(500, NameError), None


def get_tasks(current_user):
    try:
        tasks = TaskModel.select().where(TaskModel.user_id == current_user.id)

        tasks_list = list(tasks.dicts())

        return None, tasks_list
    except NameError:
        return create_error(500, NameError), None





