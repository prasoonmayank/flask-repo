from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Miguel'}
	return render_template('index.html', title='home', user=user)

@app.route('/index2')
def index2():
	user = {'user': 'Mig'}
	return render_template('index2.html', title='new title', user=user)

@app.route('/index3')
def index3():
	user = {'user': 'Miguel'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Portland'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The movie was great'
		}
		]
	return render_template('loops.html', title='change req', user=user, posts=posts)

@app.route('/index4')
def index4():
	user = {'username': 'Miguel'}
	posts = [
		{
			'author': {'username': 'Susan'},
			'body': 'Day is great'
		}
		]
	return render_template('herit.html', title='change', user=user, posts=posts)
