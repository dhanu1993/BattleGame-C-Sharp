import sqlite3
from functools import wraps
from flask import Flask, redirect, render_template, url_for, flash, request, session, g

app = Flask(__name__)
app.config.from_object('_config')
def connect_db():
	return sqlite3.connect(app.config['DATABASE_PATH'])

def login_required(test):
	@wraps
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash("You need to login first")
			return redirect(url_for('login'))
	return wrap

@app.route("/logout/")
def logout():
	session.pop('loged_in', None)
	flash("You were logged out")
	return redirect(url_for('login'))

@app.route("/", methods=["GET", 'POST'])
def login():
	error=None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = "Invalid credentials. please try again"
			return render_template('login.html', error=error)
		else:
			session['logged_in'] = True
			flash("welcome!")
			return redirect(url_for('tasks'))
	return render_template('login.html')

