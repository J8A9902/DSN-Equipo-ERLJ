from flask import Flask

from controllers.files_controller import files_blueprint

def register_blueprints(app: Flask) -> None:
    app.register_blueprint(files_blueprint)
    