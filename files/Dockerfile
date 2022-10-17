FROM python:3

RUN groupadd -r user && useradd -r -g user user
WORKDIR /files_microservice
ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD . .
RUN chown -R user:user .
RUN ["chmod", "+x", "run_service.sh"]
USER user