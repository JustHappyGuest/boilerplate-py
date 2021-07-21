from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from marshmallow import Schema, fields
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource

from task.task_service import create_task, get_tasks


class TaskListResource(MethodResource, Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='This field cannot be left blank')

    class TaskCreate(Schema):
        name = fields.String(required=True, description="Название задачи")

    class Task(Schema):
        name = fields.String(required=True, description="Название задачи")

    @jwt_required()
    @doc(description='Добавление задачи', tags=['tasks'])
    @use_kwargs(TaskCreate, location=('json'))
    @marshal_with(Task, 200)
    def post(self):
        data = self.parser.parse_args()

        name = data['name']

        error, task = create_task(name)

        if error:
            return error

        return jsonify(task)

    @jwt_required()
    @doc(description='Список задач', tags=['tasks'])
    @marshal_with(Task, 200)
    def get(self):
        error, tasks = get_tasks()

        if error:
            return error

        return jsonify(tasks)


def register_task_resources(api):
    api.add_resource(TaskListResource, '/tasks/')

def register_task_docs(docs):
    docs.register(TaskListResource)
