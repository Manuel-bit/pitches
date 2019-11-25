from flask import render_template,redirect,url_for,flash,request
from . import main
from flask_login import login_required,current_user
from .forms import PitchForm
from ..models import Pitch
from .. import db

@main.route('/')
def index():
  return render_template('index.html')


@main.route('/home')
def home():
  general = Pitch.query.all()
  return render_template('home.html',general=general)

@main.route('/pitch',methods=['GET','POST'])
@login_required
def pitch():
  form = PitchForm()
  if form.validate_on_submit():
    pitch = Pitch(title=form.title.data,pitch=form.pitch.data,category=form.category.data)
    db.session.add(pitch)
    db.session.commit()
    return redirect(url_for('main.index'))
  return render_template('pitch.html',form=form)

@main.route('/comment')
def comment():
  return render_template('comment.html')