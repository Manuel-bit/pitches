from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,validators
from wtforms.validators import DataRequired
class PitchForm(FlaskForm):
  title = StringField('Title',[validators.DataRequired()])
  pitch = TextAreaField(u'Pitch',[validators.DataRequired()])
  category = StringField('Category',[validators.DataRequired()])
  submit = SubmitField('Post')

class CommentForm(FlaskForm):
  comment = StringField('-',[validators.DataRequired()])
  Submit=SubmitField('comment')

class UpdateProfile(FlaskForm):
  bio = TextAreaField('tell us about yourself',[validators.DataRequired()])
  submit = SubmitField('Update Profile')