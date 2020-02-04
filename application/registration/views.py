from application import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required

# from application.productions.models import Production
from application.registration.forms import RegistrationForm

from application.auth.models import User

from dateutil import parser
from datetime import *

@app.route("/registration/new/", methods=["GET", "POST"])
def registration_form():
    # wanha: return render_template("shows/new.html")
    # return render_template("registration/new.html", form = RegistrationForm())
    

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, username=form.username.data, password=form.password.data)
        # user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        # flash('Congratulations, you are now a registered user!')
        return redirect(url_for("auth_login"))
    return render_template("registration/new.html", title='Register', form=form)

# @app.route("/registration/", methods=["POST"])
# def registration_create():

#     form = RegistrationForm(request.form)

#     # print("pass1: "+form.password.data)

#     if not form.validate_on_submit():
#         print("Pöö")
#         # print("pass1: "+form.password.data)
#         return render_template("registration/new.html", form = form)

#     n_name = form.name.data
#     n_uname = form.username.data
#     n_passw = form.password.data

#     n_user = User(n_name, n_uname, n_passw)
    
#     db.session().add(n_user)
#     db.session().commit()
    
#     return redirect(url_for("index"))

