from flask_jwt_extended import create_access_token

from app.core.utils.create_error import create_error
from app.core.utils.encrypt_password import encrypt_password
from app.core.constants import ACCESS_EXPIRES

from .auth_model import UserModel

def login_user(login, password):
    user = UserModel.select().where(UserModel.login == login).first()

    if not user:
        return create_error(400, 'Пользователь с таким логином не найден'), None

    password_md5 = encrypt_password(password)

    if password_md5 != user.password:
        return create_error(400, 'Пароль не подходит. Повторите попытку.'), None

    access_token = create_access_token(identity=login, expires_delta=ACCESS_EXPIRES)

    return None, {'token': access_token, 'login': login}


def register_user(login, password):

    user = UserModel.select().where(UserModel.login == login).first()

    if user:
        return create_error(400, 'Пользователь с таким логином существует'), None

    password_md5 = encrypt_password(password)

    user_created = UserModel.create(login=login, password=password_md5)
    user_created.save()

    return None, user
