from flask import Blueprint, request
from tasks import validate_uploaded_files

files_blueprint = Blueprint('files', __name__, url_prefix='/files')

@files_blueprint.route('', methods=['POST'])
def create_file():
    return "<p>Hello, World!</p>"
    