from . import auth
from flask import render_template,redirect,url_for
from .forms import SignupForm
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