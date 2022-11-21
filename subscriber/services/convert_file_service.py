from google.cloud import storage
from models import Task
from helpers.tasks_status_enum import TaskStatus


def convert_file(message: str):
    split_message = message.split(',')
    file_name = split_message[0]
    new_format = split_message[1]
    task_id = split_message[2]

    client = client = storage.Client.from_service_account_json("dsn-erlj-8549770df6f7.json")
    bucket = client.get_bucket('cloud-conversion-storage')
    
    print_file_message(file_name)

    try:
        nameTask = file_name.split('.')[0]
        blob = bucket.get_blob(file_name)
        metadata={'Content-Type':f'audio/{new_format}'}        
        blob.metadata = metadata

        blob.patch()
        bucket.rename_blob(blob, f'{nameTask}.{new_format}')

        task = Task.get_by_id(task_id)
        task.file_name = f'{nameTask}.{task.new_format}'
        task.status = TaskStatus.PROCESSED.value
        task.update()
        
        print('Convertion Successful')
        
    except Exception as e:
        return f'Error Processing File: {e}', 409


def print_file_message(file_name):
    print('-----------------------------------------------------------------')
    print(f'Processing file: {file_name} ')
    print('-----------------------------------------------------------------')
