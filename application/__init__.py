import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
login_manager = LoginManager(app)

if not os.path.exists(os.path.join(Config.UPLOAD_FOLDER, 'photos')):
    os.makedirs(os.path.join(Config.UPLOAD_FOLDER, 'photos'))

if not os.path.exists(os.path.join(os.getcwd(), 'db')):
    os.mkdir(os.path.join(os.getcwd(), 'db'))
    open(Config.SQLALCHEMY_DATABASE_URI, 'w').close()

from .views import *
