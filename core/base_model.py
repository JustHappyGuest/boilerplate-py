from peewee import Model

from core.dbs.sqlite_db import sqlit_connection


class BaseModel(Model):
    class Meta:
        database = sqlit_connection
