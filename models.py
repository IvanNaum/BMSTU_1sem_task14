from flask_login import UserMixin

from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    login = db.Column(db.String, nullable=True, unique=True)
    email = db.Column(db.String, nullable=True, unique=True)
    password = db.Column(db.String, nullable=True)
    is_admin = db.Column(db.Boolean, nullable=True, default=False)

    @staticmethod
    def add(login, email, password):
        user = User()
        user.login = login
        user.email = email
        user.password = password

        db.session.add(user)
        db.session.commit()


class Good(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    manufacturer = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String, nullable=False)

    @staticmethod
    def add(name, description, category, manufacturer, price, photo):
        good = Good()
        good.name = name
        good.description = description
        good.category = category
        good.manufacturer = manufacturer
        good.price = price
        good.photo = photo

        db.session.add(good)
        db.session.commit()

    # TODO AJAX requariment
