from peewee import CharField, ForeignKeyField

from core.base_model import BaseModel
from auth.auth_model import UserModel


class TaskModel(BaseModel):
    name = CharField()
    user = ForeignKeyField(UserModel)
