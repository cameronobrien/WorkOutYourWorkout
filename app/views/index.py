from flask import render_template

from app import app


@app.route('/index')
@app.route('/')
def index():
    return render_template(
        'index/index.html',
        page_location="Home"
    )