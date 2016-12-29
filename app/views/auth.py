from flask import render_template

from app import app


@app.route('/auth/')
def auth():
    return render_template(
        'auth/index.html',
        page_location="Login"
    )