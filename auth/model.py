from peewee import CharField

from core.base_model import BaseModel


class User(BaseModel):
    login = CharField(unique=True)
    password = CharField()
