docker rm $(docker ps -a --format "{{.Names}}" | grep microservice)
docker rm $(docker ps -a --format "{{.Names}}" | grep database)
docker rmi -f $(docker images | grep microservice)
docker-compose up --build
