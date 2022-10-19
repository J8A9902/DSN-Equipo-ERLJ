from sqlite3 import IntegrityError
from celery import Celery
from config import CELERY_BROKER
from werkzeug.utils import secure_filename
import os
from datetime import datetime, timedelta
from config import UPLOAD_FOLDER
from models import Task
from database import db
from helpers.tasks_status_enum import TaskStatus
from .flask_celery import make_celery


celery_app = Celery(__name__, broker=CELERY_BROKER)

celery_app.conf.beat_schedule = {
    'add-every-1-seconds': {
        'task': 'celery_tasks.tasks.convertir_archivos',
        'schedule': 1.0,
        'args': (16, 16)
    },
}  #minute='*/1'  crontab(sec='*/1')
celery_app.conf.timezone = 'UTC'

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


@celery_app.task(name='celery_tasks.tasks.convertir_archivos', bind=True, ignore_result=False)
def convertir_archivos(*args):
    print("convertir_archivos")
    tarea=Task.query.with_for_update().filter(Task.status=="UPLOADED").first()

    try:
        nameTask = tarea.file_name.split('.')[0]
        os.rename(UPLOAD_FOLDER+"/"+tarea.user_id+"/"+tarea.file_name, UPLOAD_FOLDER+"/"+tarea.user_id+"/"+nameTask+"."+tarea.new_format)
        ##shutil.copy(os.getcwd()+'/archivos/input/'+nombre, os.getcwd()+'/archivos/output/'+nombre)
        tarea.status="PROCESSED"
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f'Error procesando Conversión: {e}', 409