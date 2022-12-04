
# Iteration 1
- ab -v 4 -n 100 -c 10 -rk -g output.csv -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3MDA5ODI3MiwianRpIjoiM2I1NjRlMTMtNGY2ZS00YmMzLTg5NjgtYmE2NzdmZmIzMjEzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjcwMDk4MjcyLCJleHAiOjE2NzAxMTYyNzJ9.O3CWS9EB1I-N_Je22A1rpuX2pKpOoUM41HULAC5MpE8' -p post_data.txt -T "multipart/form-data; boundary=1234567890" https://hybrid-circle-368300.uc.r.appspot.com/tasks


# Iteration 2
- ab -v 4 -n 150 -c 10 -rk -g output.csv -H 'Authorization: Bearer eeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3MDEwODk0MywianRpIjoiNmI2ZTlmNjctZGFmMy00MWFiLWFiODQtM2ZjNWFiMjI5MjczIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjcwMTA4OTQzLCJleHAiOjE2NzAxMjY5NDN9.YZk5htfjWT0EnubmqbA7VXzzTZXXjcDzcghyN_zdIdA' http://34.110.214.38/api/tasks/getFile/audio.mp3 
