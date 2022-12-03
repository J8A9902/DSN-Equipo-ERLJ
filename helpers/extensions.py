from flask import Flask

from controllers.tasks_controller import tasks
from config import DATABASE_URL, UPLOAD_FOLDER
from database import db
from models import *


def initialize_database(app: Flask) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

    db.init_app(app)
    db.create_all()

def register_blueprints(app: Flask) -> None:
    app.register_blueprint(tasks)
