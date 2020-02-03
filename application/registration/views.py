from application import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required

# from application.productions.models import Production
from application.registration.forms import RegistrationForm

from application.auth.models import User

from dateutil import parser
from datetime import *

@app.route("/registration/new/")
def registration_form():
    # wanha: return render_template("shows/new.html")
    return render_template("registration/new.html", form = RegistrationForm())

@app.route("/registration/", methods=["POST"])
def registration_create():

    form = RegistrationForm(request.form)

    # if not form.validate():
    #     print("Pöö")
    #     return render_template("registration/new.html", form = form)

    n_name = form.name.data
    n_uname = form.username.data
    n_passw = form.password.data

    n_user = User(n_name, n_uname, n_passw)
    
    db.session().add(n_user)
    db.session().commit()
    
    return redirect(url_for("index"))

