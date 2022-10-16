from models.auth import Auth
from werkzeug.security import generate_password_hash


def create(auth_object):
    message: str = ''
    status: int = 200

    try:
        encrypted_password = generate_password_hash(auth_object['password'])
        new_auth = Auth(auth_object['user_id'], auth_object['email'], encrypted_password)
        new_auth.save()

        message = f'Authentication for {new_auth.email} Created Successfully'

    except Exception as e:
        status = 500
        message = f'Error: {e}'

    return { 'message': message, 'status': status }
        