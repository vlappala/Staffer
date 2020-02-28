from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField
from wtforms.fields.html5 import TimeField

class ProductionForm(FlaskForm):
    
    name = StringField("Production name", [validators.Length(min=2, max=100)])

    show_duration = TimeField("Show duration", [validators.InputRequired()])
    misc_info = TextAreaField("Miscellaneous information", [validators.Length(max=2000)])

    

    class Meta:
        csrf = False
