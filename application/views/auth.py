from flask import render_template, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from application import app, login_manager
from application.forms import LoginForm, RegisterForm
from application.models import User


@app.route('/login', methods=['GET', 'POST'])
def login_view():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))

    return render_template('login.html', form=form, title='Войти')


@app.route('/register', methods=['GET', 'POST'])
def register_view():
    form = RegisterForm()

    if form.validate_on_submit():
        login = form.login.data
        email = form.email.data
        password = form.password1.data

        if not form.check_email():
            flash('Этот email уже занят')
        elif not form.check_login():
            flash('Этот логин уже занят')
        else:
            User.add(login=login,
                     email=email, password=generate_password_hash(password))

            return redirect(url_for('login_view'))
    return render_template('register.html', form=form, title='Регистрация')


@app.route("/logout")
@login_required
def logout_view():
    logout_user()
    return redirect('index')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
