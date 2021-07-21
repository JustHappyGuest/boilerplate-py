from flask_jwt_extended import JWTManager
from os import environ

from core.dbs.redis_db import redis_connection

SECRET = environ.get("SECRET")


def create_jwt(app):
    app.config["JWT_SECRET_KEY"] = SECRET
    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_is_revoked(_, jwt_payload):
        jti = jwt_payload["jti"]
        token_in_redis = redis_connection.get(jti)
        return token_in_redis is not None

    return jwt