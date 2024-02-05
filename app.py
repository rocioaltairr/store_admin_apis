from flask import Flask
from flask_smorest import Api
from flask_cors import CORS

import models

from db import db
from resources.item import blp as ItemBlueprint
from resources.account import blp as AccountBlueprint
from resources.tag import blp as TagBlueprint

def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Accounts REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    api = Api(app)

    # Enable CORS for all routes
    CORS(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(AccountBlueprint)
    api.register_blueprint(TagBlueprint)

    return app
