from task.task_model import TaskModel
from auth.auth_model import UserModel


def init_db():
    TaskModel.create_table()
    UserModel.create_table()
