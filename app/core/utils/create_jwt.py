from flask_jwt_extended import JWTManager
from os import environ
from playhouse.shortcuts import model_to_dict

from app.core.dbs.redis_db import redis_connection
from app.auth.auth_model import UserModel

SECRET = environ.get("SECRET")


def create_jwt(app):
    app.config["JWT_SECRET_KEY"] = SECRET
    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_is_revoked(_, jwt_payload):
        jti = jwt_payload["jti"]
        token_in_redis = redis_connection.get(jti)
        return token_in_redis is not None
    
    @jwt.user_lookup_loader
    def user_lookup_callback(_, jwt_data):
        identity = jwt_data["sub"]

        user = UserModel.get_or_none(UserModel.login == identity)
        
        if not user:
            return None

        return user

    return jwt