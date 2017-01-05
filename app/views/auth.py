"""
User API for authentication
"""

from flask import render_template, current_app, request, flash, url_for, redirect, session, abort, jsonify

from flask_login import login_required, login_user, current_user, logout_user, confirm_login, login_fresh

from app import app, db
from ..forms.admin.accounts.login import LoginForm
from ..forms.admin.accounts.register import RegistrationForm
from ..exceptions import Response
from ..models.user import User


@app.route('/auth',)
def auth():
    return render_template(
        'auth/index.html',
        page_title="Login"
    )


@auth.route('/verify_auth', methods=['GET'])
@login_required
def verify_auth():
    return Response.make_data_resp(data=current_user.to_json())


@auth.route('/login', methods=['POST'])
def login():
    """ POST only operation. check login form. Log user in """
    if current_user.is_authenticated():
        return Response.make_success_resp(msg="You are already logged in")

    form = LoginForm()
    if form.validate_on_submit():
        user, authenticated = User.authenticate(form.username.data,
                                                form.password.data)
        if user:
            if authenticated:
                login_user(user, remember=form.remember_me.data)
                return Response.make_data_resp(data=current_user.to_json(), msg="You have successfully logged in")
            else:
                return Response.make_error_resp(msg="Invalid username or password", type="Wrong Authentication",
                                                code=422)
        else:
            return Response.make_error_resp(msg="Username does not exist", type="Wrong Authentication", code=422)

    return Response.make_form_error_resp(form=form)


@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    """ logout user """
    session.pop('login', None)
    logout_user()
    return Response.make_success_resp(msg="You have successfully logged out")


@auth.route('/signup', methods=['POST'])
def signup():
    def signup():
        if current_user.is_authenticated():
            return Response.make_success_resp("You're already signed up")

        form = RegistrationForm()

        if form.validate_on_submit():
            # check if user_name or email is taken
            if User.is_user_name_taken(form.username.data):
                return Response.make_error_resp(msg="This username is already taken!", code=409)
            if User.is_email_taken(form.email.data):
                return Response.make_error_resp(msg="This email is already taken!", code=409)

            try:
                # create new user
                user = User()
                form.populate_obj(user)

                db.session.add(user)
                db.session.commit()

            except Exception as e:
                return Response.make_exception_resp(exception=e)

            # log the user in
            login_user(user)
            return Response.make_success_resp(
                msg="You successfully signed up!")

        return Response.make_form_error_resp(form=form)



