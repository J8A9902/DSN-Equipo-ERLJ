from hashlib import new

import requests

from models.user import User
from config.config import AUTH_SERVICE_URL


def create(user):
    message: str = ''
    status: int = 200

    try:
        new_user = User(user['username'])
        new_user.save()

        create_auth(user, new_user.id)

        message = f'User {new_user.username} Created Successfully'

    except Exception as e:
        status = 500
        message = f'Error: {e}' 

    return { 'message': message, 'status': status }

def create_auth(user, user_id):
    request_object = { 'id': user_id, 'email': user['email'], 'password': user['password'] }
    requests.post(f'{AUTH_SERVICE_URL}/auth/create', json=request_object)

    