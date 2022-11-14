from flask import Blueprint, jsonify, request, send_from_directory

from services.tasks_service import *
from authentication import login_required

tasks = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks.route('', methods=['GET'])
@login_required
def get_tasks(user_id: int):
    data = request.json
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


@tasks.route('/getFile/<string:name_task>', methods=['GET'])
def get_file(name_task: str):
    client = client = storage.Client.from_service_account_json("dsn-erlj-8549770df6f7.json")
    bucket = client.get_bucket('cloud-conversion-storage')
    try:
        
        task = Task.query.filter(Task.file_name==name_task).first()
        print("--------------------------------------------------")
        print("Entro acá 1")
        print(name_task)
        if(task):
            blob = bucket.get_blob(name_task)
            print("--------------------------------------------------")
            print("Entro acá")
            print(blob)
            ##file_path = f'{UPLOAD_FOLDER}/{str(task.user_id)}'
            return "Funciono"
        else:
            return { 'message': "No existe el registro", 'status': status }
    except Exception as e:
        status = 500
        message = f'Error: {e}'
        return { 'message': message, 'status': status }  
