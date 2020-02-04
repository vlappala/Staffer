from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from application.auth.models import User

# ...

class RegistrationForm(FlaskForm):

    name = StringField('Name', [validators.Length(min=2)])
    username = StringField('Username', [validators.Length(min=2)])
    # email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', [validators.DataRequired()])
    password2 = PasswordField(
        'Repeat Password', [validators.DataRequired(), validators.EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            print("Jee")
            raise ValidationError('Please use a different username.')

    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user is not None:
    #         raise ValidationError('Please use a different email address.')



# Wanhaa:

# from flask_wtf import FlaskForm
# from wtforms import PasswordField, StringField
  
# class RegistrationForm(FlaskForm):
#     username = StringField("Username")
#     password = PasswordField("Password")
#     password_again = PasswordField("Password again")
  
#     class Meta:
#         csrf = False