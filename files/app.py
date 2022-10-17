from flask import Flask

from helpers.extensions import register_blueprints


app: Flask = Flask(__name__)


with app.app_context():
    register_blueprints(app)
