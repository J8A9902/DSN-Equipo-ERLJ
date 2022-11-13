import os
from flask import Flask
from helpers.extensions import initialize_database

from celery import Celery
from config import CELERY_BROKER, UPLOAD_FOLDER
from models import Task
from google.cloud import storage

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
    client = client = storage.Client.from_service_account_json("dsn-erlj-8549770df6f7.json")
    bucket = client.get_bucket('cloud-conversion-storage')
    tasks=Task.query.with_for_update().filter(Task.status=="UPLOADED")
    for task in tasks:
        if(task):
            print_file_message(task.file_name)
        try:
            nameTask = task.file_name.split('.')[0]
            blob = bucket.get_blob(task.file_name)
            metadata={'Content-Type':'audio/'+task.new_format}
            blob.metadata = metadata
            blob.patch()

            bucket.rename_blob(blob, nameTask+'.'+ task.new_format)

            task.file_name = nameTask+'.'+ task.new_format
            task.status = TaskStatus.PROCESSED.value
            task.update()
            
        except Exception as e:
            task.rollback()
            return f'Error procesando Conversión: {e}', 409
        else:
            print('Exitoso!!!!!!!')

def print_file_message(file_name):
    print('-----------------------------------------------------------------')
    print(f'Processing file: {file_name} ')
    print('-----------------------------------------------------------------')