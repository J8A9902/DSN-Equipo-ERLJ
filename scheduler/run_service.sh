while !</dev/tcp/34.121.35.36/5432;
do sleep 1;
done;
celery -A app.celery_app beat & 
celery -A app.celery_app worker -l  info
