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
from app import app

celery_app = Celery(__name__, broker=CELERY_BROKER)

   
celery_app= make_celery(app.py)

app.config['CELERYBEAT_SCHEDULE'] = {
    # Executes every minute
    'periodic_task-every-minute': {
        'task': 'celery_tasks.tasks.convertir_archivos',
        'schedule': timedelta(seconds=1)
    }
}
celery_app.conf.timezone = 'UTC'

@celery_app.task()
def convertir_archivos():
    print("convertir_archivos")
    tarea=Task.query.with_for_update().filter(Task.status=="UPLOADED").first()
    if tarea is None:
        return 'Error procesando Conversión', 409

    try:
        nameTask = tarea.file_name.split('.')[0]
        os.rename(UPLOAD_FOLDER+"/"+tarea.user_id+"/"+tarea.file_name, UPLOAD_FOLDER+"/"+tarea.user_id+"/"+nameTask+"."+tarea.new_format)
        ##shutil.copy(os.getcwd()+'/archivos/input/'+nombre, os.getcwd()+'/archivos/output/'+nombre)
        tarea.status="PROCESSED"
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return 'Error procesando Conversión', 409