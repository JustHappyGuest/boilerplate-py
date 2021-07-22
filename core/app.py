import os
from flask import Flask
from flask_restful import Api
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

from core.register_resources import register_resources
from core.utils.init_db import init_db
from core.utils.create_jwt import create_jwt


APP_TITLE = os.environ.get("APP_TITLE")

def create_app():
    app = Flask(__name__)

    init_db()
    create_jwt(app)
    register_resources(Api(app))

    return app