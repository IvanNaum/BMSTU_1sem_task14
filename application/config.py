import os


class Config:
    DEBUG = True
    SECRET_KEY = "JwtYGjqwNzRbwnNmHeWs2i63liQ6e8qR"

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'db', 'data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'application/static')
