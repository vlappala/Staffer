from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from application.auth.models import User

# ...

class RegistrationForm(FlaskForm):

    name = StringField('Name', [validators.Length(min=2, max=100)])
    username = StringField('Username', [validators.Length(min=2, max=100)])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=2, max=100)])
    password2 = PasswordField(
        'Repeat Password', [validators.DataRequired(), validators.Length(min=2, max=100), validators.EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            print("Jee")
            raise ValidationError('Please use a different username.')

