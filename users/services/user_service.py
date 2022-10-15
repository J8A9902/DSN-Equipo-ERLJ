from hashlib import new

from models.user import User


def create(user):
    message: str = ''
    status: int = 200

    try:
        new_user = User(user['username'], user['email'], user['password'])
        new_user.save()

        message = f'User {new_user.username} Created Successfully'

    except Exception as e:
        status = 500
        message = f'Error: {e}' 

    return { 'message': message, 'status': status }
    