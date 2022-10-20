from flask import Flask

from helpers.extensions import register_blueprints, initialize_database

from celery import Celery
from config import CELERY_BROKER


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
        'schedule': 1.0,
        'args': ('prueba')
    },
}  #minute='*/1'  crontab(sec='*/1')
celery_app.conf.timezone = 'UTC'

@celery_app.task(name='convertir_archivos',bind=True)
def convertir_archivos(*args):
     print("convertir_archivos")




