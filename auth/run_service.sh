while !</dev/tcp/34.121.35.36/5432; 
do sleep 5; 
done;
gunicorn -b 0.0.0.0:5000 app:app
