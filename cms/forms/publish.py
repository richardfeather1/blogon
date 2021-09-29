from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, length


class new_story(FlaskForm):
    title = StringField("Story Title.", validators=[DataRequired(), length(max=30)])
    body = TextAreaField("Story Body.", validators=[DataRequired()])
    image = FileField("Story image.")
