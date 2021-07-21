from task.model import Task
from auth.model import User


def init_db():
    Task.create_table()
    User.create_table()
