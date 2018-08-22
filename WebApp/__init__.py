import os

from flask import Flask, render_template
from .model import register as register_models
from flask_sqlalchemy import SQLAlchemy
from .views import register as register_views

from .space import AssetStorage, ChallengeStorage

def create_app(test_config=None):
    global db
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db = SQLAlchemy(app)
    register_models(db)
    register_views(app)
    app.db = db

    app.challenge_storage = ChallengeStorage(app, "challenge")
    app.asset_storage = AssetStorage(app, "asset")
    
    return app
