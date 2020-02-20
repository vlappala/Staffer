from application import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.shows.models import Show
from application.shows.forms import ShowForm

from application.workshift.models import Shift



from dateutil import parser
from datetime import *

@app.route("/shows/", methods=["GET"])
@login_required
def shows_index():

    shows = Show.find_basic_show_info()

    return render_template("shows/list.html", shows=shows)

@app.route("/shows/new/")
@login_required
def shows_form():

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


    t = Show(s_name, showtime)
    t.open_for_recruitment = form.show_open_for_recruitment.data


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


@app.route("/workshift/<show_id>/", methods=["POST"])
@login_required
def shows_hand_up(show_id):


    shiftExists = Shift.get_instance(current_user.id, show_id)
    print()
    print("HALOO!!!")
    print()
    print("SHIFTSin koko: ", shiftExists)
    if (shiftExists < 1):

        shift=Shift(current_user.id, show_id)
        db.session().add(shift)
        db.session().commit()

    

  
    return redirect(url_for("list_open_shows"))

@app.route("/shows/open_shows/", methods=["GET"])
@login_required
def list_open_shows():

    shiftIds = Shift.getShowIdsByUserId(current_user.id)

    return render_template("shows/open_shows/list.html", shows = Show.query.all(), shiftIds=shiftIds)

@app.route("/shows/information/<show_id>/", methods=["GET"])
@login_required
def show_information(show_id):

    
    show = Show.query.get(show_id)
    
      
    return render_template("shows/information/showinfo.html", show = show)