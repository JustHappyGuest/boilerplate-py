from app.task.task_model import TaskModel
from app.auth.auth_model import UserModel
from app.core.dbs.sqlite_db import sqlite_connection


def init_db():
    sqlite_connection.create_tables([TaskModel, UserModel])
