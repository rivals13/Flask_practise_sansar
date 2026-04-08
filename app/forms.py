from flask_wtf import FlaskForm  # the class  for the form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Email

class LoginForm(FlaskForm): #  the login form class
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])  # first argument is  the  label for the  form
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm): #  the register form class
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])  # first argument is  the  label for the  form
    # Email = StringField('Email', validators=[DataRequired(), Email()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign UP!')
