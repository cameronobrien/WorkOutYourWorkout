from flask import Blueprint, render_template


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/<path>')
def verifyauth():
    return render_template('auth/index.html')
