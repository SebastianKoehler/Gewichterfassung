from flask import Flask
from flask_migrate import Migrate

from app.config import Config
from app.database import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from app.models import WeightEntry
        from app.routes import app_routes

        app.register_blueprint(app_routes)

    return app
