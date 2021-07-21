from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt, jwt_required
from marshmallow import Schema, fields
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource

from auth.auth_service import register_user, login_user
from core.dbs.redis_db import redis_connection
from core.constants import ACCESS_EXPIRES

class UserCreate(Schema):
    login = fields.String(required=True, description="Имя пользователя")
    password = fields.String(required=True, description="Пароль")

class User(Schema):
    name = fields.String(required=True, description="Имя пользователя")
    token = fields.String(required=True, description="JWT Токен")

class UserResource(MethodResource, Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('login', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')

    @doc(description='Авторизация', tags=['auth'])
    @use_kwargs(UserCreate, location=('json'))
    @marshal_with(User, 200)
    def get(self):
        data = self.parser.parse_args()

        login = data['login']
        password = data['password']

        error, result = login_user(login, password)

        if error:
            return error

        return result


class UserRegisterResource(MethodResource, Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('login', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')

    @doc(description='Регистрация', tags=['auth'])
    @use_kwargs(UserCreate, location=('json'))
    @marshal_with(User, 201)
    def post(self):
        data = self.parser.parse_args()

        login = data['login']
        password = data['password']

        error, _ = register_user(login, password)

        if error:
            return jsonify(error)

        return {'login': login}, 201


class UserLogoutResource(MethodResource, Resource):
    @jwt_required()
    @doc(description='Удаление токена', tags=['auth'])
    def post(self):
        jti = get_jwt()["jti"]
        redis_connection.set(jti, "", ex=ACCESS_EXPIRES)
        return jsonify(msg="Access token revoked")


def register_auth_resources(api):
    api.add_resource(UserRegisterResource, '/register/')
    api.add_resource(UserResource, '/login/')
    api.add_resource(UserLogoutResource, '/logout/')

def register_auth_docs(docs):
    docs.register(UserResource)
    docs.register(UserRegisterResource)
    docs.register(UserLogoutResource)
