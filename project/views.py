import sqlite3
from flask import Flask, redirect, url_for, render_template, session, request, flash 
from functools import wraps

#configurations
app = Flask(__name__)
app.config.from_object("_config")

def connect_db():
	return sqlite3.connect(app.config['DATABASE_PATH'])

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash("You need to login first")
			return redirect(url_for('login'))
	return wrap

@app.route("/logout/")
def logout():
	session.pop('logged_in', None)
	flash("Goodbye!")
	return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = "Invalid Credentials. please try again"
			return render_template('login.html', error=error)
		else:
			session['logged_in'] = True
			flash("Welcome.")
			return redirect(url_for('tasks'))
	return render_template('login.html')

@app.route("/tasks/")
@login_required
def main():
	pass
