from flask import render_template, url_for, redirect
from flask_login import login_user, logout_user, login_required, current_user

from app import app, db, lm
from app.auth.forms import LoginForm, RegisterForm
from app.auth.models import User
from app.helpers import get_current_time
import hashlib
m = hashlib.sha512()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(username=form.login.data).first()

        if user and user.password == form.password.data:
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


@app.route('/register' ,methods=['GET', 'POST'])
def register():
    global m
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User(
            user_name = form.username.data,
            email = form.email.data,
            created_on = get_current_time(),
            _password = m.update(form.password.data.encode('utf-8'))
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('index'))

    return render_template(
        'auth/index.html',
        form=form,
    )



