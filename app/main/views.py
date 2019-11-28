from flask import render_template,redirect,url_for,flash,request,abort
from . import main
from flask_login import login_required,current_user
from .forms import PitchForm,CommentForm,UpdateProfile
from ..models import Pitch,Comment,User
from .. import db

@main.route('/')
def index():
  return render_template('index.html')


@main.route('/home',methods=['GET','POST'])
@login_required
def home():
  general = Pitch.query.all()
  return render_template('home.html',general=general)


@main.route('/pitch',methods=['GET','POST'])
@login_required
def pitch():
  user = current_user.id
  form = PitchForm()
  if form.validate_on_submit():
    pitch = Pitch(title=form.title.data,pitch=form.pitch.data,category=form.category.data,user_id=user)
    db.session.add(pitch)
    db.session.commit()
    return redirect(url_for('main.home'))
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
  interview = Pitch.query.filter_by(category = 'interview').all()
  return render_template('interview.html',interview=interview)

@main.route('/comment/<id>',methods=['GET','POST'])
def comment(id):
  user = current_user.id
  pitch = Pitch.query.filter_by(id=id).first()
  form = CommentForm()
  if form.validate_on_submit():
    cmt = Comment(comment=form.comment.data,user_id=user,pitch_id=id)
    db.session.add(cmt)
    db.session.commit()
    comments = Comment.query.filter_by(pitch_id=id).all()
    return render_template('comment.html',pitch=pitch,form=form,commenst=comments)
  comments = Comment.query.filter_by(pitch_id=id).all()
  return render_template('comment.html',form=form,pitch=pitch,comments=comments)

@main.route('/user/<uname>')
@login_required
def profile(uname):
  cUser = current_user.id
  pitches = Pitch.query.filter_by(id=cUser).all()
  user = User.query.filter_by(username=uname).first()

  if user is None:
    abort(404)
  
  return render_template('profile.html',user=user,pitches=pitches)


