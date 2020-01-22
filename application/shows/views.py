from application import app, db
from flask import redirect, render_template, request, url_for
from application.shows.models import Show

@app.route("/shows/", methods=["GET"])
def shows_index():
    return render_template("shows/list.html", shows = Show.query.all())

@app.route("/shows/new/")
def shows_form():
    return render_template("shows/new.html")
  
# @app.route("/shows/<show_id>/", methods=["POST"])
# def tasks_set_done(show_id):

    # t = Show.query.get(show_id)
    # b = t.done
    
    # t.done = not b
    # db.session().commit()
  
    # return redirect(url_for("tasks_index"))

@app.route("/shows/", methods=["POST"])
def shows_create():

    date = request.form.get("showdate")
    t = Show(request.form.get("name"), date)
    # show_time = Show(request.form.get("showtime"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("shows_index"))