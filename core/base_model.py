from peewee import Model

from core.dbs.sqlite_db import sqlite_connection


class BaseModel(Model):
    class Meta:
        database = sqlite_connection
