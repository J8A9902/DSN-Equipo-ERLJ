import os
from flask import Flask
from helpers.extensions import register_blueprints, initialize_database
import shutil

from celery import Celery
from config import CELERY_BROKER, UPLOAD_FOLDER
from models import Task

from helpers.tasks_status_enum import TaskStatus



app=Flask(__name__)
  
def make_celery(app):
    celery=Celery(__name__,backend = CELERY_BROKER, broker=CELERY_BROKER)
    celery.conf.update(app.config)
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task=ContextTask
    return celery


app_context=app.app_context()
app_context.push()

register_blueprints(app)
initialize_database(app)

celery_app=make_celery(app)
celery_app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'convertir_archivos',
        'schedule': 30.0,
        'args': ('prueba')
    },
}  
celery_app.conf.timezone = 'UTC'

@celery_app.task(name='convertir_archivos',bind=True)
def convertir_archivos(*args):
    task=Task.query.with_for_update().filter(Task.status=="UPLOADED").first()

    if(task):
        print_file_message(task.file_name)

        try:
            nameTask = task.file_name.split('.')[0]

            os.rename(f'{UPLOAD_FOLDER}/{task.user_id}/{task.file_name}', \
                f'{UPLOAD_FOLDER}/{task.user_id}/{nameTask}.{task.new_format}')

        
            task.status = TaskStatus.PROCESSED.value
            task.update()
            
        except Exception as e:
            task.rollback()
            return f'Error procesando Conversión: {e}', 409
    else:
        print('No Files to be processed')


def print_file_message(file_name):
    print('-----------------------------------------------------------------')
    print(f'Processing file: {file_name} ')
    print('-----------------------------------------------------------------')