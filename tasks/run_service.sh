while !</dev/tcp/tasks-database/5432;
do sleep 1;
done;
celery -A app.celery_app beat & 
celery -A app.celery_app worker -l  info & gunicorn -b 0.0.0.0:5000 app:app
