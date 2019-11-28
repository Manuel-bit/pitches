from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model,UserMixin):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255))
  pass_secure = db.Column(db.String(255))
  bio= db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  pitches= db.relationship('Pitch',backref = 'user',lazy='dynamic')
  comment = db.relationship('Comment',backref= 'user',lazy='dynamic')


  def password(self,password):
    self.pass_secure = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)

  


  def __repr__(self):
    return f'User {self.username}'

class Pitch(db.Model):
  __tablename__ = 'pitches'
  id = db.Column(db.Integer,primary_key = True)
  title = db.Column(db.String(255),nullable = False)
  pitch = db.Column(db.String(500),nullable = False)
  category = db.Column(db.String(255),nullable = False)
  votes = db.Column(db.Integer)
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  comments = db.relationship('Comment',backref='pitch',lazy='dynamic')


class Comment(db.Model):
  __tablename__ = 'comments'
  id = db.Column(db.Integer, primary_key=True)
  comment = db.Column(db.String(500))
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))  
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

