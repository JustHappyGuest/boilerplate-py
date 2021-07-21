from task.task_model import Task
from auth.auth_model import User


def init_db():
    Task.create_table()
    User.create_table()
