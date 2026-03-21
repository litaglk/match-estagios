from dotenv import load_dotenv
from flask import Flask
from flask_mvc import FlaskMVC

from .config import Config
from .extensions import db, migrate

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    FlaskMVC(app, "match_estagios")

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    return app
