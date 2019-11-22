from . import db

class User(db.Model):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255))
  pass_secure = db.Column(db.String(255))
  