from flask import Blueprint, jsonify, request

from services.tasks_service import get_all_tasks_by_user, create_new_task, get_task_by_id, get_all_uploaded_tasks
from authentication import login_required

tasks = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks.route('', methods=['GET'])
@login_required
def get_tasks(user_id: int):
    response = get_all_tasks_by_user(user_id)

    return jsonify(response), response['status']


@tasks.route('', methods=['POST'])
@login_required
def create_task(user_id):
    uploaded_file = request.files['fileName']
    new_format = request.form['newFormat']

    response = create_new_task(user_id, uploaded_file, new_format)

    return jsonify(response), response['status']


@tasks.route('/<int:id_task>', methods=['GET'])
def get_task(id_task: int):
    response = get_task_by_id(id_task)   

    return jsonify(response), response['status']


@tasks.route('/uploads', methods=['GET'])
def get_all_tasks_uploads():
    response = get_all_uploaded_tasks()

    return jsonify(response), response['status']
