from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, URL


class AddSourceForm(FlaskForm):
    source = StringField('Source', validators=[DataRequired(), URL(message='invalid url')])
    title = StringField('Title')