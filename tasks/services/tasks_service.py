import string
from models import *
from helpers.utils import object_as_dict
from celery_tasks import *
import os
from config import UPLOAD_FOLDER
from flask import send_file

def get_all_tasks_by_user(user_id: int, requestData):
    message: list = []
    status: int = 200
    max = requestData['max']
    order = requestData['order']

    try:
       if(order != 1 and order != 0):
            raise Exception('Order not valid')

       tasks = Task.limit_get_all(user_id, max, order)

       for i in range(len(tasks)):
            task = object_as_dict(tasks[i])
            message.append(task)

    except Exception as e:
        status = 500
        message = f'Error: {e}'


    return { 'message': message , 'status': status }


def create_new_task(user_id, upload_file, new_format):
    message: str = ''
    status: int = 200

    try:
        new_task = Task(upload_file.filename, user_id, new_format)
        new_task.save()

        create_file(upload_file, new_task.id, user_id)
    
        message = f'Task for change the extension of file: {upload_file.filename} to {new_format} was created'
       
    except Exception as e:
        status = 500
        message = f'Error: {e}'


    return { 'message': message, 'status': status }


def get_task_by_id(user_id, id_task: int):
    message: str = ''
    status: int = 200

    try:
        task = Task.get_by_id(id_task)

        if(task.user_id != user_id):
            raise Exception(f'User not authorized for this action')

        message = object_as_dict(task)
        
    except Exception as e:
        status = 500
        message = f'Error: {e}'


    return { 'message': message, 'status': status }


def delete_task(user_id: int, task_id: int):
    message: str = ''
    status: int = 200
    task = Task.get_by_id(task_id)

    try:
        if(task.user_id != user_id):
            raise Exception(f'User not authorized for this action')

        task.delete()

        message = f'Task with id: {task_id} deleted seccessfully'
        
    except Exception as e:
        status = 500
        message = f'Error: {e}'


    return { 'message': message, 'status': status }


def update_task(user_id: int, task_id: int, new_format: str):
    message: str = ''
    status: int = 200
    task = Task.get_by_id(task_id)

    try:
        if(task.user_id != user_id):
            raise Exception(f'User not authorized for this action')

        task.new_format = new_format
        task.status = TaskStatus.UPLOADED.value

        task.update()

        message = f'Task with id: {task_id} updated seccessfully'
        
    except Exception as e:
        status = 500
        message = f'Error: {e}'


    return { 'message': message, 'status': status }

def get_file_by_name(name_task: string):
    message: str = ''
    status: int = 200
    print("------------------------------------jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    try:
        task = Task.query.filter(Task.file_name==name_task).first()
        if(task):
            file_path = os.path.join(f'uploads/{task.user_id}', task.file_name)
            print(file_path)
            print(name_task)
            return send_file(file_path, as_attachment=True)
        else:
            return { 'message': "No existe el registro", 'status': status }
    except Exception as e:
        status = 500
        message = f'Error: {e}'
        return { 'message': message, 'status': status }