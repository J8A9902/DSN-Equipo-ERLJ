from flask import Blueprint

users = Blueprint('user', __name__, url_prefix='/users')

@users.route('/', methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"
    