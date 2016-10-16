from flask import render_template, request
from website import app, models, db
from flask_sqlalchemy import SQLAlchemy
import sys

from .models import cpu, motherboard

clist = ["cpu", "motherboard"]

@app.route('/')
@app.route('/index')
@app.route('/categories')
def index():
	return render_template('index.html', clist = clist)

@app.route('/category/<cname>')
def list_items( cname ):

	# Gets the class module depending on the category chosen.
	cque = getattr(sys.modules[__name__], cname)
	# Queries the
	products = db.session.query(cque).all()

	return render_template('list_products.html', products = products, category = cname)

@app.route('/category/<cname>/<pid>')
def show_product( cname, pid ):

	return "Hello " + cname + "    id: " + pid

