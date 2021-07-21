from peewee import CharField
from core.base_model import BaseModel


class Task(BaseModel):
    name = CharField()
