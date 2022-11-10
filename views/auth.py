from flask import render_template
from flask_login import login_required

from app import app, login_manager
from forms import LoginForm, RegisterForm
from models import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        ...

    return render_template('login.html', form=form, title='Войти')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        ...

    return render_template('register.html', form=form, title='Регистрация')


@app.route('/logout')
@login_required
def logout():
    ...


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
