from copy import error
from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, current_user
import jwt
from .task_model import TaskModel
from .task_service import create_task, get_tasks, delete_task, update_task


class TaskListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='This field cannot be left blank')

    @jwt_required()
    def post(self):
        data = self.parser.parse_args()

        name = data['name']

        error, task = create_task(current_user, name)

        if error:
            return error

        return jsonify(task)

    @jwt_required()
    def get(self):
        error, tasks = get_tasks(current_user)

        if error:
            return error

        return jsonify(tasks)

class TaskResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='This field cannot be left blank')

    @jwt_required()
    def delete(self, task_id):
        
        error = delete_task(current_user, task_id)

        if error:
           return error

        return jsonify({'task_id': task_id})

    @jwt_required()
    def patch(self, task_id):

        data = self.parser.parse_args()

        name = data['name']
        
        error, task = update_task(current_user, task_id, name)

        if error:
            return error
        
        return jsonify(task)

def register_task_resources(api):
    api.add_resource(TaskListResource, '/tasks/')
    api.add_resource(TaskResource, '/task/<string:task_id>')