from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import ValidationError, DataRequired, Length
  
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=100)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=2, max=100)])
  
    class Meta:
        csrf = False