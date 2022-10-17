import os

DATABASE_URL = os.environ.get('DATABASE_URL')
FILES_MICROSERVICE = os.environ.get('FILES_MICROSERVICE')
CELERY_BROKER = os.environ.get('CELERY_BROKER')
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

