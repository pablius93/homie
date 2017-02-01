from passlib.hash import pbkdf2_sha256 as sha256


def hash_password(password):
    return sha256.hash(password)


def verify_password(password, user_hash):
    return sha256.verify(password, user_hash)
