import os

from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(
    __name__,
    static_folder="../client/build",
    static_url_path="/",
    template_folder="../client/build"
)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

app.secret_key = os.environ.get("SECRET_KEY")

db = SQLAlchemy()
migrate = Migrate(app, db)

bcrypt = Bcrypt(app)

db.init_app(app)

Api.error_router = lambda self, handler, e: handler(e)
api = Api(app)