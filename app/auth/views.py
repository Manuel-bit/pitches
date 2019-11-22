from . import auth
from flask import render_template,redirect
from .forms import SignupForm
from ..models import User

@auth.route('/signup',methods = ["GET","POST"])
def signup():
  form = SignupForm()
  if form.validate_on_submit():
    user = User(username=form.username.data,email=form.email.data,pass_secure=form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('main.index'))
  title='Sign up'
  return render_template('signup.html',form=form,title=title)