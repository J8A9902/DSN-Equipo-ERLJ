from flask import Flask

from config import DATABASE_URL, GCP_PROJECT_ID, GCP_SUBSCRIPTION_ID
from database import db
from models import *
from sub.subscriber import receive_messages


def initialize_database(app: Flask) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

    db.init_app(app)

def receive_publisher_messages(app: Flask):
    while True:
        message = receive_messages(GCP_PROJECT_ID, GCP_SUBSCRIPTION_ID, app)
        print('---------------------')
        print(message)
