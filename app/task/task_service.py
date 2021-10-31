from re import T
from playhouse.shortcuts import model_to_dict

from app.core.utils.create_error import create_error

from .task_model import TaskModel

def create_task(current_user, name):
    try:
        task = TaskModel.create(user_id=current_user.id, name=name)
        task.save()


        return None, {"name": task.name, "id": task.id}
    except NameError:
        return create_error(500, NameError), None


def get_tasks(current_user):
    try:
        tasks = TaskModel.select(TaskModel.name, TaskModel.id).where(TaskModel.user_id == current_user.id)

        tasks_list = list(tasks.dicts())

        return None, tasks_list
    except NameError:
        return create_error(500, NameError), None


def delete_task(current_user, task_id):
    try:
        task = TaskModel.get(TaskModel.user_id == current_user.id, TaskModel.id == task_id)

        task.delete_instance()
    except NameError:
        return create_error(500, NameError), None


def update_task(current_user, task_id, new_name):
    try:
        task = TaskModel.select()\
            .where(TaskModel.user_id == current_user.id, TaskModel.id == task_id).get()
        
        task.name = new_name
        task.save()

        return None, {"name": task.name, "id": task.id}
    except NameError:
        return create_error(500, NameError), None
