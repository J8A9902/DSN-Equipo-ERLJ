from celery import Celery
from config import CELERY_BROKER

celery_app = Celery(__name__, broker=CELERY_BROKER)

@celery_app.task()
def upload_file(file_name: str):
    print('celery is running!!!!!')
    with open('test_log.txt', 'a+') as file:
        file.write(f'Uploaded file: {file_name}')