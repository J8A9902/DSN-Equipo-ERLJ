from flask import Blueprint, request
from tasks import upload_file

files_blueprint = Blueprint('files', __name__, url_prefix='/files')

@files_blueprint.route('/create', methods=['POST'])
def create_file():

   

    return "<p>Hello, World!</p>"
    