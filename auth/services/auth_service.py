from models.auth import Auth


def create(auth_object):
    message: str = ''
    status: int = 200
    new_auth = Auth(auth_object['user_id'], auth_object['email'], auth_object['password'])

    try:
        new_auth.save()

        message = f'Authentication for {new_auth.email} Created Successfully'

    except Exception as e:
        status = 500
        message = f'Error: {e}'
        new_auth.rollback()

    return { 'message': message, 'status': status }
        