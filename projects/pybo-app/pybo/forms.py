from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired(), Length(max=200)])
    content = TextAreaField('내용', validators=[DataRequired()])


class AnswerForm(FlaskForm):
    content = TextAreaField('답변내용', validators=[DataRequired()])
