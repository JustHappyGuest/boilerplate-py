from peewee import CharField, ForeignKeyField

from app.core.base_model import BaseModel
from app.auth.auth_model import UserModel


class TaskModel(BaseModel):
    name = CharField()
    user = ForeignKeyField(UserModel)
