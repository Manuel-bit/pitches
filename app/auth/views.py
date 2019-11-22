from . import auth
from flask import render_template,redirect,url_for,flash,request
from .forms import SignupForm,LoginForm
from ..models import User
from .. import db

@auth.route('/signup',methods = ["GET","POST"])
def signup():
  title='Sign up'
  form = SignupForm()
  if form.validate_on_submit():
    user = User(username=form.username.data,email=form.email.data,pass_secure=form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('main.index'))
  return render_template('signup.html',form=form,title=title)

@auth.route('/login')
def login():
  title='Log In'
  form = LoginForm()
  if form.validate_on_submit():
    user = User.querry.filter_by(email = form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user,form.remeber.data)
      return redirect(request.args.get('next') or url_for('main.index'))
    flash('invalid username or password')
  return render_template('login.html',title=title,form=form)