from app import app
from  flask import render_template
from app.posts import posts
from dotenv import load_dotenv
import  os
from app.forms import RegisterForm

load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'you-will-never-guess'

@app.route('/')
def index():
    user = {'username': 'Sansar'}

    return render_template('index.html',title="Home",user=user,posts=posts)
@app.route('/register')

def register():
    form =RegisterForm()
    # user = {'username': 'Sansar'}

    return render_template('register.html',title="register",form=form)