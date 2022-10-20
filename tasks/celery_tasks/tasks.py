import os
from celery import Celery
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER, CELERY_BROKER
from helpers.tasks_status_enum import TaskStatus
from models import Task

celery_app = Celery(__name__, broker=CELERY_BROKER)

@celery_app.task()
def create_file(uploaded_file, task_id, user_id):
    if(uploaded_file and uploaded_file.filename):
        try:
            file_name = secure_filename(uploaded_file.filename)
            file_path = os.path.join(f'{UPLOAD_FOLDER}/{user_id}', file_name)

            if(not os.path.exists(file_path)):
                os.makedirs(file_path)

            
            uploaded_file.save(os.path.join(UPLOAD_FOLDER, file_name))

            task = Task.get_by_id(task_id)

            task.status = TaskStatus.UPLOADED.value
            task.update()

        except Exception as e:
            raise Exception('Error uploading the file, please try again')
    else:
        raise Exception('File not provided')