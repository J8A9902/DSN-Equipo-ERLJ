from flask import Flask
from flask_jwt_extended import JWTManager

from controllers.auth_controller import auth
from config.config import DATABASE_URL
from database import db
from models import *


def initialize_database(app: Flask) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

    db.init_app(auth)
    db.create_all()


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(users)


def setup_jwt(app: Flask) -> None:
    app.config["JWT_SECRET_KEY"] = "super-secret"
    jwt = JWTManager(app)
    