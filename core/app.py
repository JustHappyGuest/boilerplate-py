from flask import Flask
from flask_restful import Api

from core.register_resources import register_resources
from core.init_db import init_db
from core.create_jwt import create_jwt


def create_app():
    app = Flask(__name__)

    init_db()
    create_jwt(app)
    api = Api(app)
    register_resources(api)

    return app