from functools import wraps
from urllib import response
import requests
from config import AUTH_SERVICE

import flask


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        headers = flask.request.headers
        auth = headers['Authorization']
        request_headers = {'Authorization': auth}
        response = requests.get(f'{AUTH_SERVICE}/auth/whoami', headers=request_headers)
        response_json = response.json()

        if(response.status_code != 200):
            return response_json

        return f(*args, **kwargs)
    return decorated_function