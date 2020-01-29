from application import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.shows.models import Show
from application.shows.forms import ShowForm

from dateutil import parser
from datetime import *

@app.route("/shows/", methods=["GET"])
@login_required
def shows_index():
    return render_template("shows/list.html", shows = Show.query.all())

@app.route("/shows/new/")
@login_required
def shows_form():
    # wanha: return render_template("shows/new.html")
    return render_template("shows/new.html", form = ShowForm())
  
@app.route("/shows/<show_id>/", methods=["POST"])
@login_required
def shows_set_recruitment_open(show_id):

    t = Show.query.get(show_id)
    b = t.open_for_recruitment
    
    t.open_for_recruitment = not b
    db.session().commit()
  
    return redirect(url_for("shows_index"))

@app.route("/shows/", methods=["POST"])
@login_required
def shows_create():

    form = ShowForm(request.form)

    if not form.validate():
        return render_template("shows/new.html", form = form)


    s_name = form.name.data
    showtime = ""
    showtime = showtime + form.showdate.data.strftime("%Y-%m-%d")
    showtime = showtime + " "
    showtime = showtime + form.showtime.data.strftime("%H:%M")
    showtime = parser.parse(showtime)

    # showtime = datetime.now()

    # s_name = request.form.get("name")
    # showtime = request.form.get("showdate")
    # showtime = showtime + " "
    # showtime = showtime + request.form.get("showtime")
    # showtime = parser.parse(showtime)


    # date = request.form.get("showdate")
    # wanha: t = Show(request.form.get("name"), date)
    t = Show(s_name, showtime)
    t.open_for_recruitment = form.show_open_for_recruitment.data
    # show_time = Show(request.form.get("showtime"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("shows_index"))