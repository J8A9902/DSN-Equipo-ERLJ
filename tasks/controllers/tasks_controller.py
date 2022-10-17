from flask import Blueprint, jsonify, request

from services.tasks_service import get_all_tasks, create_new_task, get_task_by_id
from werkzeug.utils import secure_filename
import os

from config import UPLOAD_FOLDER


tasks = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks.route('', methods=['GET'])
def get_tasks():
    response = get_all_tasks()

    return jsonify(response), response['status']


@tasks.route('', methods=['POST'])
def create_task():
    print(request.files['fileName'].filename, 'rrrrrrrrrrrrrrrrrrrr')
    print(UPLOAD_FOLDER, 'ÑÑÑÑÑÑ')
    uploaded_file = request.files['fileName']
    new_format = request.form['newFormat']

    if(uploaded_file and uploaded_file.filename):
        file_name = secure_filename(uploaded_file.filename)
        uploaded_file.save(os.path.join(UPLOAD_FOLDER, file_name))

    return jsonify({'data':  'HOLA'}), 200


@tasks.route('/<int:id_task>', methods=['GET'])
def get_task(id_task: int):
    response = get_task_by_id(id_task)   

    return jsonify(response), response['status'] 