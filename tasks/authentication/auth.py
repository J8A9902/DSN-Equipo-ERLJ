import flask
from functools import wraps
import requests
from config import AUTH_SERVICE


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        headers = flask.request.headers

        if('Authorization' in headers):
            auth = headers['Authorization']
            request_headers = {'Authorization': auth}
            response = requests.get(f'{AUTH_SERVICE}/auth/whoami', headers=request_headers)
            response_json = response.json()

            if(response.status_code != 200):
                return response_json
        else:
            return flask.jsonify({'message': 'Not authorized'}), 401

        return f(response_json['logged_in_as'], *args, **kwargs)
    return decorated_function