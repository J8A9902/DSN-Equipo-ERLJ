from flask import Blueprint, jsonify, request

users = Blueprint('user', __name__, url_prefix='/users')
from services.user_service import create

@users.route('/create', methods=['POST'])
def create_user():
    data = request.json
    response = create(data)

    return jsonify(response), response['status']
    