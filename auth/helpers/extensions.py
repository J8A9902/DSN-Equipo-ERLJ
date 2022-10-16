from datetime import timedelta
from flask import Flask

from controllers.auth_controller import auth_blueprint
from config.config import DATABASE_URL
from database import db
from models import *
from flask_jwt_extended import JWTManager

def initialize_database(app: Flask) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

    db.init_app(app)
    db.create_all()

def register_blueprints(app: Flask) -> None:
    app.register_blueprint(auth_blueprint)

def setup_jwt(app: Flask) -> None:
    app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=5)
    