import os
from flask import Flask
from flask_restful import Api
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

from core.register_resources import register_resources
from core.utils.init_db import init_db
from core.utils.create_jwt import create_jwt
from core.register_docs import register_docs


APP_TITLE = os.environ.get("APP_TITLE")

def create_app():
    app = Flask(__name__)

    init_db()
    create_jwt(app)
    register_resources(Api(app))


    app.config.update({
        'APISPEC_SPEC': APISpec(
            title=APP_TITLE,
            version='v1',
            plugins=[MarshmallowPlugin()],
            openapi_version='2.0.0'
        ),
        'APISPEC_SWAGGER_URL': '/swagger-json/',
        'APISPEC_SWAGGER_UI_URL': '/swagger/'
    })

    register_docs(FlaskApiSpec(app))

    return app