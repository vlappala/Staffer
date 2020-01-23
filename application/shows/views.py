from application import app, db
from flask import redirect, render_template, request, url_for
from application.shows.models import Show
from dateutil import parser
from datetime import *

@app.route("/shows/", methods=["GET"])
def shows_index():
    return render_template("shows/list.html", shows = Show.query.all())

@app.route("/shows/new/")
def shows_form():
    return render_template("shows/new.html")
  
@app.route("/shows/<show_id>/", methods=["POST"])
def shows_set_recruitment_open(show_id):

    t = Show.query.get(show_id)
    b = t.open_for_recruitment
    
    t.open_for_recruitment = not b
    db.session().commit()
  
    return redirect(url_for("shows_index"))

@app.route("/shows/", methods=["POST"])
def shows_create():

    # showtime = datetime.now()
    s_name = request.form.get("name")
    showtime = request.form.get("showdate")
    showtime = showtime + " "
    showtime = showtime + request.form.get("showtime")
    showtime = parser.parse(showtime)

    # date = request.form.get("showdate")
    # wanha: t = Show(request.form.get("name"), date)
    t = Show(s_name, showtime)
    # show_time = Show(request.form.get("showtime"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("shows_index"))