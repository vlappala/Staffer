# flask-sovellus

from flask import Flask
app = Flask(__name__)

# tietokanta

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shows.db"    
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)


# kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

from flask import redirect, url_for

# roles in login_required
from functools import wraps

def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            acceptable_roles = set(("ANY", *current_user.roles()))

            if role not in acceptable_roles:
                return redirect(url_for('index'))

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)





# oman sovelluksen toiminnallisuudet

from application import views

from application.shows import models
from application.shows import views

from application.productions import models
from application.productions import views

from application.auth import models
from application.auth import views

from application.workshift import models

from application.admin import views

from application.registration import views

from application.roles import models



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
  
try: 
    db.create_all()
except:
    pass