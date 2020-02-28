from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.fields.html5 import DateField, TimeField

class ShowForm(FlaskForm):
    
    name = StringField("Show name", [validators.Length(min=2, max=100)])
    showdate = DateField("Showdate", [validators.InputRequired()])
    showtime = TimeField("Showtime", [validators.InputRequired()])
    



    class Meta:
        csrf = False

