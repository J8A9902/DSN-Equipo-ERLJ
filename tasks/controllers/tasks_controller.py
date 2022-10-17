from flask import Blueprint, jsonify, request

from services.tasks_service import get_all_tasks, create_new_task, get_task_by_id

tasks = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks.route('', methods=['GET'])
def get_tasks():
    response = get_all_tasks()

    return jsonify(response), response['status']


@tasks.route('', methods=['POST'])
def create_task():
    data = request.json
    response = create_new_task(data)

    return jsonify(response), response['status']


@tasks.route('/<int:id_task>', methods=['GET'])
def get_task(id_task: int):
    response = get_task_by_id(id_task)   

    return jsonify(response), response['status'] 