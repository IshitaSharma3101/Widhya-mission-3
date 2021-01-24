from flask import render_template
from app import app
from app.main import ReviewForm

# ...

@app.route('/review')
def review():
    form = ReviewForm()
    return render_template('form.html', title='Review', form=form)