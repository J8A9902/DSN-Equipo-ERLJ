from flask import Blueprint, jsonify, request

from services.tasks_service import get_all_tasks, create_new_task

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
    