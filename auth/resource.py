from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt, jwt_required

from auth.service import register_user, login_user
from core.dbs.redis_db import redis_connection
from core.constants import ACCESS_EXPIRES


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('login', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')

    def get(self):
        data = self.parser.parse_args()

        login = data['login']
        password = data['password']

        error, result = login_user(login, password)

        if error:
            return error

        return result


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('login', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')

    def post(self):
        data = self.parser.parse_args()

        login = data['login']
        password = data['password']

        error, _ = register_user(login, password)

        if error:
            return jsonify(error)

        return {'login': login}, 201


class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        redis_connection.set(jti, "", ex=ACCESS_EXPIRES)
        return jsonify(msg="Access token revoked")


def register_auth_resources(api):
    api.add_resource(UserRegister, '/register/')
    api.add_resource(User, '/login/')
    api.add_resource(UserLogout, '/logout/')




