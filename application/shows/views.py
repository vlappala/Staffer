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

@app.route("/shows/delete/<show_id>/", methods=["POST"])
@login_required
def shows_delete(show_id):



    t = Show.query.get(show_id)
    db.session.delete(t)
    
    
    db.session().commit()
  
    return redirect(url_for("shows_index"))

@app.route("/shows/details/<show_id>/", methods=["GET"])
@login_required
def show_details(show_id):

    form = ShowForm()
    show = Show.query.get(show_id)
    form.name.data = show.name
      
    return render_template("shows/details/new.html", show = show, form = form)

@app.route("/shows/details/update/<show_id>/", methods=["POST"])
@login_required
def show_update(show_id):

    form = ShowForm(request.form)
    show = Show.query.get(show_id)

    if not form.validate():
        return render_template("shows/details/new.html", show = show, form = form)


    show.name = form.name.data
    
    showtime = ""
    showtime = showtime + form.showdate.data.strftime("%Y-%m-%d")
    showtime = showtime + " "
    showtime = showtime + form.showtime.data.strftime("%H:%M")
    showtime = parser.parse(showtime)

    show.show_date = showtime
    show.open_for_recruitment = form.show_open_for_recruitment.data
    db.session().commit()
  
    return redirect(url_for("shows_index"))

  
# Ei toimi: 

# @app.route("/shows/details/edit/<show_id>/", methods=["GET"])
# @login_required
# def edit_show_details(show_id):

#     show = Show.query.get(show_id)

#     formi = ShowForm()

  
  
#     return render_template("shows/details/edit/editform.html", form = formi, show = show)


