from flask import Flask, render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import DataRequired
from csv import writer
import pandas as pd

def append_list_as_row(list_of_elem):
    with open('data.csv', 'a+', newline='') as obj:
        csv_writer = writer(obj)
        csv_writer.writerow(list_of_elem)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'scadsdasbbasjbcjasbjcbask'

class ReviewForm(FlaskForm):
    fname = StringField('User Name *', validators=[DataRequired()])
    pname = StringField('Product Name *', validators=[DataRequired()])
    review = TextAreaField('Review *', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ReviewForm()
    if form.validate_on_submit():
        print(form.fname.data)
        record = [form.fname.data, form.pname.data, form.review.data]
        append_list_as_row(record)
        return redirect(url_for('home'))
    return render_template('home.html', form=form, reviews=pd.read_csv('data.csv'))


if __name__ == '__main__':
    app.run(debug=True)