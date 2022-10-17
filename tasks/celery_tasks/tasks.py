from celery import Celery
import requests
from config import FILES_MICROSERVICE, CELERY_BROKER

celery_app = Celery(__name__, broker=CELERY_BROKER)

@celery_app.task()
def create_file(file_name: str):
    request_object = { 'fileName': file_name }
    response = requests.post(f'{FILES_MICROSERVICE}/files/create', json=request_object)
