from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['POST'])
def login():
    return "<p>Hello, World!</p>"
    