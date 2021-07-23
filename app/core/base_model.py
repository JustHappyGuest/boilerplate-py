from peewee import Model

from .dbs.postgres_db import postgresql_connection


class BaseModel(Model):
    class Meta:
        database = postgresql_connection
