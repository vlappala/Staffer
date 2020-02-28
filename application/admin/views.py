from application import app, db, login_required
from flask import render_template
from application.workshift.models import Shift

@app.route("/admin/")
@login_required(role="ADMIN")
def admin_pages():

    # signups contains two items per show: Total number of signups per show and an instance of that Show 

    signups = Shift.find_shifts_with_sign_ups()

 

    return render_template("admin/index.html", signups=signups)

