from peewee import Model

from .dbs.sqlite_db import sqlite_connection


class BaseModel(Model):
    class Meta:
        database = sqlite_connection
