from flask import Blueprint, jsonify, request

from services.tasks_service import *
from authentication import login_required

tasks = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks.route('', methods=['GET'])
@login_required
def get_tasks(user_id: int):
    data = response.json
    response = get_all_tasks_by_user(user_id, data)

    return jsonify(response), response['status']


@tasks.route('', methods=['POST'])
@login_required
def create_task(user_id: int):
    uploaded_file = request.files['fileName']
    new_format = request.form['newFormat']

    response = create_new_task(user_id, uploaded_file, new_format)

    return jsonify(response), response['status']


@tasks.route('/<int:id_task>', methods=['GET'])
@login_required
def get_task(user_id: int, id_task: int):
    response = get_task_by_id(user_id, id_task)   

    return jsonify(response), response['status']



@tasks.route('/<int:id_task>', methods=['DELETE'])
@login_required
def delete(user_id: int, id_task: int):
    response = delete_task(user_id, id_task)

    return jsonify(response), response['status']



@tasks.route('/<int:id_task>', methods=['PUT'])
@login_required
def update(user_id: int, id_task: int):
    data = request.json
    new_format = data['newFormat']
    
    response = update_task(user_id, id_task, new_format)

    return jsonify(response), response['status']
