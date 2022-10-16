from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required, create_access_token
from services.auth_service import create

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    access_token = create_access_token(identity=data['email'])
    
    return jsonify(access_token=access_token)


@auth_blueprint.route('/whoami', methods=['GET'])
@jwt_required()
def whoami():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@auth_blueprint.route('/create', methods=['POST'])
def create_auth():
    data = request.json

    response = create(data)

    return jsonify(response), response['status']
