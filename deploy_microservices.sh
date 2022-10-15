docker rm $(docker ps -aq) -f
docker rmi -f week1_users-microservice 
docker-compose up
