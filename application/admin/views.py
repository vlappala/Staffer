from application import app, db, login_required

from flask import redirect, render_template, request, url_for

# from flask_login import login_required

from application.productions.models import Production
from application.productions.forms import ProductionForm

from application.shows.models import Show
from application.shows.forms import ShowForm

from application.workshift.models import Shift


from dateutil import parser
from datetime import *

@app.route("/admin/")
@login_required(role="ADMIN")
def admin_pages():

    signups = Shift.find_shifts_with_sign_ups()

 

    return render_template("admin/index.html", signups=signups)

