from models.user import User
from werkzeug.security import generate_password_hash


def create_user(user):
    message: str = ''
    status: int = 200

    if(user['password1'] == user['password2']):
        try:
            encrypted_password = generate_password_hash(user['password1'])
            new_user = User(user['username'], user['email'], encrypted_password)
            new_user.save()

            message = f'User {new_user.email} Created Successfully'

        except Exception as e:
            status = 500
            message = f'Error: {e}'
    else:
        message = 'The passwords does not match'
        status = 400

    return { 'message': message, 'status': status }
        