import datetime

from flask import render_template

from app import app


@app.route('/auth/')
def auth():
    return render_template(
        'auth/index.html',
        page_title="Login"
    )
# @app.route('/auth/register', methods=['GET','POST'])
# http://flask.pocoo.org/docs/0.12/patterns/sqlalchemy/#sqlalchemy-pattern

