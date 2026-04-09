from app import app, db
from flask import render_template
from app.forms import RegisterForm

@app.route('/')
def index():
    user = {'username': 'Sansar'}
    return render_template('index.html', title="Home", user=user)

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', title="register", form=form)