from flask import render_template, url_for, redirect
from flask_login import login_user, logout_user, current_user

from app import app, db
from app.auth.forms import LoginForm, RegisterForm
from app.auth.models import User
from app.helpers import hash_password


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(username=form.login.data).first()

        if user and user.password == hash_password(form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))

    return render_template(
        'auth/index.html',
        form=form,
    )


@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('index'))
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User(
            user_name=form.username.data,
            email=form.email.data,
            password=hash_password(form.data.password)
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('index'))

    return render_template(
        'auth/index.html',
        form=form,
    )
