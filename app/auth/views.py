from flask import render_template, url_for, redirect
from flask_login import login_user, logout_user, current_user, login_required

from app import app, db
from app.auth.forms import LoginForm, RegisterForm
from app.auth.models import User
from app.helpers import hash_password, check_password
import bcrypt


@app.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_authenicated:
        return redirect(url_for('login'))
    return render_template(
        'index/dashboard.html'
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.user_name == form.login.data).first()

        print(form.login.data)
        print(form.password.data)
        print(user.password)
        print(hash_password(form.password.data, user.salt))
        if user and check_password(hash_password(form.password.data, user.salt), user.password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            print("something was wrong with the way you tried to log in")

    return render_template(
        'auth/login.html',
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
    if form.is_submitted():
        print("submitted")
    if form.validate():
        print("valid")
    print(form.errors)
    if form.validate_on_submit():
        user = User(
            user_name=form.username.data,
            email=form.email.data,
            user_salt=bcrypt.gensalt(12),
            password=hash_password(form.password.data, user_salt)
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('dashboard'))

    return render_template(
        'auth/register.html',
        form=form,
    )
