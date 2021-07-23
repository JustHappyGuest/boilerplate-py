from app.task.task_model import TaskModel
from app.auth.auth_model import UserModel
from app.core.dbs.postgres_db import postgresql_connection


def init_db():
    postgresql_connection.create_tables([TaskModel, UserModel])
