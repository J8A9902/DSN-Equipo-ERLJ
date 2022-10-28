while !</dev/tcp/tasks-database/5432;
do sleep 1;
done;
gunicorn -b 0.0.0.0:5000 app:app
