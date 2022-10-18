from flask import Blueprint, jsonify, request

from services.tasks_service import get_all_tasks, create_new_task, get_task_by_id
from authentication import login_required

tasks = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks.route('', methods=['GET'])
@login_required
def get_tasks():
    response = get_all_tasks()

    return jsonify(response), response['status']


@tasks.route('', methods=['POST'])
def create_task():
    uploaded_file = request.files['fileName']
    new_format = request.form['newFormat']

    response = create_new_task(uploaded_file, new_format)

    return jsonify(response), response['status']


@tasks.route('/<int:id_task>', methods=['GET'])
def get_task(id_task: int):
    response = get_task_by_id(id_task)   

    return jsonify(response), response['status'] 