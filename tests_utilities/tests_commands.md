
# Iteration 1
- ab -v 4 -n 100 -c 10 -rk -g output.csv -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3MDA5ODI3MiwianRpIjoiM2I1NjRlMTMtNGY2ZS00YmMzLTg5NjgtYmE2NzdmZmIzMjEzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjcwMDk4MjcyLCJleHAiOjE2NzAxMTYyNzJ9.O3CWS9EB1I-N_Je22A1rpuX2pKpOoUM41HULAC5MpE8' -p post_data.txt -T "multipart/form-data; boundary=1234567890" https://hybrid-circle-368300.uc.r.appspot.com/tasks


# Iteration 2
- ab -v 4 -n 150 -c 10 -rk -g output.csv -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2OTAwMDU4NywianRpIjoiZjA0MjY2M2YtMWYxNi00MWI5LThmYTItOThjODQ3OGYzN2ZlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjY5MDAwNTg3LCJleHAiOjE2NjkwMTg1ODd9.2TftBfXAtTzwvZS0aj4ad-yMzTqhJ2YZOAGtqx1K18w' http://34.110.214.38/api/tasks/getFile/audio.ogg 
