import os

DATABASE_URL = os.environ.get('DATABASE_URL')
AUTH_SERVICE = os.environ.get('AUTH_SERVICE')
UPLOAD_FOLDER = '/nfs/home'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
