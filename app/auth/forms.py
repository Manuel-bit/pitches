from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,validators
from wtforms.validators import EqualTo,DataRequired

class SignupForm(FlaskForm):
  username = StringField('User Name',[validators.DataRequired()])
  email = StringField('Email',[validators.DataRequired()])
  password = PasswordField('Password',[validators.DataRequired(), validators.EqualTo("confirm", message='passwords must match')])
  confirm = PasswordField('Confir Password',[validators.DataRequired()])
  submit = SubmitField('Sign Up')