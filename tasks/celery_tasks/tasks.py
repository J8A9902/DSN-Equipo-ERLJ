from celery import Celery
from config import CELERY_BROKER
from werkzeug.utils import secure_filename
import os

from config import UPLOAD_FOLDER
from models.task import Task
from helpers.tasks_status_enum import TaskStatus

celery_app = Celery(__name__, broker=CELERY_BROKER)

@celery_app.task()
def create_file(uploaded_file, task_id):
    if(uploaded_file and uploaded_file.filename):
        try:
            file_name = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join(UPLOAD_FOLDER, file_name))

            task = Task.get_by_id(task_id)

            task.status = TaskStatus.UPLOADED
            task.update()

        except Exception as e:
            raise Exception('Error uploading the file, please try again')
    else:
        raise Exception('File not provided')
