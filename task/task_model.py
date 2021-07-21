from peewee import CharField
from core.base_model import BaseModel


class TaskModel(BaseModel):
    name = CharField()
