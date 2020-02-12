from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators
from wtforms.fields.html5 import DateField, TimeField, DateTimeField

class ProductionForm(FlaskForm):
    
    name = StringField("Production name", [validators.Length(min=2)])

    # showtime = TimeField("Showtime", [validators.InputRequired()])

    

    class Meta:
        csrf = False
