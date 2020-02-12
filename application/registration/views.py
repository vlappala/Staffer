from application import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required


from application.registration.forms import RegistrationForm

from application.auth.models import User

from dateutil import parser
from datetime import *

@app.route("/registration/new/", methods=["GET", "POST"])
def registration_form():


    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth_login"))
    return render_template("registration/new.html", title='Register', form=form)

