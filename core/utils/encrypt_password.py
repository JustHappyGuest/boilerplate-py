from hashlib import sha512


def encrypt_password(password):
    salt = "salt"

    password_md5 = sha512(password.encode() + salt.encode()).hexdigest()

    return password_md5
