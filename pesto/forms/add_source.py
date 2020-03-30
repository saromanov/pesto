from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class AddSourceForm(FlaskForm):
    source = StringField('Source', validators=[DataRequired(])