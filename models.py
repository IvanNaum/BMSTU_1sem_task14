from flask_login import UserMixin

from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    login = db.Column(db.String, nullable=True, unique=True)
    email = db.Column(db.String, nullable=True, unique=True)
    password = db.Column(db.String, nullable=True)
