from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ReviewForm(FlaskForm):
    fname = StringField('FirstName', validators=[DataRequired()])
    product = StringField('Product', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')