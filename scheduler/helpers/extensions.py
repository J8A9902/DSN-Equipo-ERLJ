from flask import Flask

from config import DATABASE_URL
from database import db
from models import *


def initialize_database(app: Flask) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

    db.init_app(app)
