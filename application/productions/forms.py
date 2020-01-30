from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators
from wtforms.fields.html5 import DateField, TimeField, DateTimeField

class ProductionForm(FlaskForm):
    
    name = StringField("Production name", [validators.Length(min=2)])
    # showdate = DateField("Showdate", [validators.InputRequired()])
    # showtime = TimeField("Showtime", [validators.InputRequired()])
    # show_open_for_recruitment =  BooleanField("Open for recruitment")

    # test = DateTimeField("testiloota", [validators.InputRequired()])
    

    class Meta:
        csrf = False
