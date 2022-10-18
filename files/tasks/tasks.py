from celery import Celery
from config import CELERY_BROKER

celery_app = Celery(__name__, broker=CELERY_BROKER)

@celery_app.task()
def validate_uploaded_files():
    pass
    