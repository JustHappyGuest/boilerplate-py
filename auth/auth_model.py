from peewee import CharField

from core.base_model import BaseModel


class UserModel(BaseModel):
    login = CharField(unique=True)
    password = CharField()
