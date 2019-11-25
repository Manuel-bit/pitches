from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,validators
from wtforms.validators import DataRequired
class PitchForm(FlaskForm):
  title = StringField('Title',[validators.DataRequired()])
  pitch = TextAreaField('Pitch',[validators.DataRequired()])
  category = StringField('Category',[validators.DataRequired()])
  submit = SubmitField('Post')