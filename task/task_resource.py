from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from task.task_service import create_task, get_tasks


class TaskListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='This field cannot be left blank')

    @jwt_required()
    def post(self):
        data = self.parser.parse_args()

        name = data['name']

        error, task = create_task(name)

        if error:
            return error

        return jsonify(task)

    @jwt_required()
    def get(self):
        error, tasks = get_tasks()

        if error:
            return error

        return jsonify(tasks)


def register_task_resources(api):
    api.add_resource(TaskListResource, '/tasks/')