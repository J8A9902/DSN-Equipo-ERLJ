from turtle import delay
from flask import Blueprint, request
from tasks.tasks import upload_file

files_blueprint = Blueprint('files', __name__, url_prefix='/files')

@files_blueprint.route('/create', methods=['POST'])
def create_file():
    data = request.json
    file_name = data['fileName']

    upload_file.delay(file_name)

    return "<p>Hello, World!</p>"
    