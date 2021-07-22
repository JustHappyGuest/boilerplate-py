import os
from flask import Flask
from flask_restful import Api

from .dbs.sqlite_db import sqlite_connection
from .register_resources import register_resources
from .utils.init_db import init_db
from .utils.create_jwt import create_jwt
from .constants import API_PREFIX


APP_TITLE = os.environ.get("APP_TITLE")

def create_app():
    app = Flask(__name__)

    init_db()
    register_resources(Api(app, prefix=API_PREFIX))
    create_jwt(app)

    @app.before_request
    def before_request():
        sqlite_connection.connect()

    @app.after_request
    def after_request(response):
        sqlite_connection.close()
        return response


    return app