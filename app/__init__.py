from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    # Get project root directory
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, 'templates'),
        static_folder=os.path.join(base_dir, 'static')
    )

    app.config.from_object('config.Config')

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app