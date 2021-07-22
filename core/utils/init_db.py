from task.task_model import TaskModel
from auth.auth_model import UserModel
from core.dbs.sqlite_db import sqlite_connection


def init_db():
    sqlite_connection.create_tables([TaskModel, UserModel])
