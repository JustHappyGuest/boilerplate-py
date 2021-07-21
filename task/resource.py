from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from task.service import create_task, get_tasks


class Task(Resource):
    @jwt_required()
    def delete(self, task_id):
        return task_id
        # task = filter(lambda t: t['id'] == task_id, tasks)
        # if len(task) == 0:
        #     abort(404)
        # return jsonify({'task': task[0]})


class TaskList(Resource):
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

    # @jwt_required()
    def get(self):
        error, tasks = get_tasks()

        if error:
            return error

        return jsonify(tasks)


def register_task_resources(api):
    api.add_resource(Task, '/task/<task_id>')
    api.add_resource(TaskList, '/tasks/')
