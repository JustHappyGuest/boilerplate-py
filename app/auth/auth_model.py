from peewee import CharField

from app.core.base_model import BaseModel


class UserModel(BaseModel):
    login = CharField(unique=True)
    password = CharField()
