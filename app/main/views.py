from flask import render_template,redirect,url_for,flash,request
from . import main
from flask_login import login_required,current_user
from .forms import PitchForm,CommentForm
from ..models import Pitch,Comment
from .. import db

@main.route('/')
def index():
  return render_template('index.html')


@main.route('/home',methods=['GET','POST'])
def home():
  form = CommentForm()
  print(current_user)
  if form.validate_on_submit():
    comment = Comment(comment=form.comment.data)
    db.session.add(comment)
    db.session.commit()
  general = Pitch.query.all()
  return render_template('home.html',general=general,form=form)


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

@main.route('/fun')
def fun():
  form = CommentForm()
  fun = Pitch.query.filter_by(category = 'fun').all()
  return render_template('fun.html',fun=fun,form=form)

@main.route('/pick_up')
def pick_up():
  form = CommentForm()
  pick_up_lines = Pitch.query.filter_by(category = 'pick up line').all()
  return render_template('pick-up.html',pick_up_lines=pick_up_lines,form=form)

@main.route('/inteview')
def inteview():
  form = CommentForm()
  interview = Pitch.query.filter_by(category = 'inteview').all()
  return render_template('interview.html',interview=interview,form=form)


