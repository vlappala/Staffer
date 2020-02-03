from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import ValidationError, DataRequired
  
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
  
    class Meta:
        csrf = False