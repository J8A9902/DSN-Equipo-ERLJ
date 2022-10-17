from flask import jsonify
from models import Task
from helpers.utils import object_as_dict


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


def create_new_task(task):
    message: str = ''
    status: int = 200
    file_name = task['fileName']
    new_format = task['newFormat']
    
    try:
       new_task = Task(file_name, 1, new_format)
       new_task.save()

       message = f'Task for change the extension of file: {file_name} to {new_format} was created'
       
    except Exception as e:
        status = 500
        message = f'Error: {e}'


    return { 'message': message, 'status': status }

