from flask import render_template, request
from website import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"
