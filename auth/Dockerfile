FROM python

RUN groupadd -r user && useradd -r -g user user
WORKDIR /auth_microservice
ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD . .
RUN chown -R user:user .
USER user