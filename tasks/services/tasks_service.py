from models import *
from helpers.utils import object_as_dict
from celery_tasks import *

def get_all_tasks():
    message: list = []
    status: int = 200

    try:
       tasks = Task.get_all()

       for i in range(len(tasks)):
            task = object_as_dict(tasks[i])
            message.append(task)

    except Exception as e:
        status = 500
        message = f'Error: {e}'


    return { 'message': message , 'status': status }


def create_new_task(upload_file, new_format):
    message: str = ''
    status: int = 200

    try:
        new_task = Task(upload_file.filename, 1, new_format)
        new_task.save()

        create_file(upload_file, new_task.id)
    
        message = f'Task for change the extension of file: {upload_file.filename} to {new_format} was created'
       
    except Exception as e:
        status = 500
        message = f'Error: {e}'


    return { 'message': message, 'status': status }


def get_task_by_id(id_task: int):
    message: str = ''
    status: int = 200

    try:
        task = Task.get_by_id(id_task)
        message = object_as_dict(task)
        
    except Exception as e:
        status = 500
        message = f'Error: {e}'


    return { 'message': message, 'status': status }
