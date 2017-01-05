"""
   Users API for authentication
"""
from flask import session, render_template

from flask_login import login_required, login_user, current_user, logout_user
from app.exceptions import response
from app import db, app
from app.models.user import User
from app.forms.admin.accounts.login import LoginForm
from app.forms.admin.accounts.register import RegistrationForm


@app.route('/auth/verify_auth', methods=['GET', 'POST'])
@login_required
def verify_auth():
    # return response.make_data_resp(data=current_user.to_json())
    return render_template('auth/index.html')


@app.route('/auth/login', methods=['GET', 'POST'])
def login():  
    """ POST only operation. check login form. Log user in """
    if current_user.is_authenticated:
        return response.make_success_resp(msg="You are already logged in")

    form = LoginForm()
    if form.validate_on_submit():
        user, authenticated = User.authenticate(form.login.data,
                                                form.password.data)
        if user:
            if authenticated:
                login_user(user, remember=form.remember_me.data)
                return response.make_data_resp(data=current_user.to_json(), msg="You have successfully logged in")
            else:
                return response.make_error_resp(msg="Invalid username or password", err_type="Wrong Authentication", code=422)
        else:
            return response.make_error_resp(msg="Username does not exist", err_type="Wrong Authentication", code=422)

    return response.make_form_error_resp(form=form)


@app.route('/auth/logout', methods=['GET', 'POST'])
@login_required
def logout():  
    """ logout user """
    session.pop('login', None)
    logout_user()
    return response.make_success_resp(msg="You have successfully logged out")


@app.route('/auth/signup', methods=['GET', 'POST'])
def signup():  
    if current_user.is_authenticated:
        return response.make_success_resp("You're already signed up")

    form = RegistrationForm()

    if form.validate_on_submit():
        # check if user_name or email is taken
        if User.is_user_name_taken(form.user_name.data):
            return response.make_error_resp(msg="This username is already taken!", code=409)
        if User.is_email_taken(form.email.data):
            return response.make_error_resp(msg="This email is already taken!", code=409)

        try:
            # create new user
            user = User()
            form.populate_obj(user)

            db.session.add(user)
            db.session.commit()

        except Exception as e:
            return response.make_exception_resp(exception=e)

        # log the user in
        login_user(user)
        return response.make_success_resp(msg="You successfully signed up!")

    return response.make_form_error_resp(form=form)