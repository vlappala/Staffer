from application import app, db, login_required

from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.shows.models import Show
from application.shows.forms import ShowForm

from application.workshift.models import Shift, ShiftDetails





from dateutil import parser
from datetime import *

@app.route("/shows/", methods=["GET"])
@login_required(role="ADMIN")
def shows_index():


    return render_template("shows/list.html", shows=Show.query.order_by(Show.show_date).all())

@app.route("/shows/new/")
@login_required(role="ADMIN")
def shows_form():

    return render_template("shows/new.html", form = ShowForm())
  

@app.route("/shows/", methods=["POST"])
@login_required(role="ADMIN")
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


    show = Show(s_name, showtime)
    


    db.session().add(show)
    db.session().commit()
  
    return redirect(url_for("shows_index"))

@app.route("/shows/delete/<show_id>/", methods=["POST"])
@login_required(role="ADMIN")
def shows_delete(show_id):

    shiftIds = Shift.find_shiftIds_by_showId(show_id)

    for shiftId in shiftIds:
        
        shiftdetails = ShiftDetails.query.get(shiftId)
        db.session.delete(shiftdetails)
        db.session.commit()

        shift = Shift.query.get(shiftId)
        db.session.delete(shift)
        db.session.commit()

    show = Show.query.get(show_id)
    db.session.delete(show)
    
    
    db.session().commit()
  
    return redirect(url_for("shows_index"))

@app.route("/shows/details/<show_id>/", methods=["GET"])
@login_required(role="ADMIN")
def show_details(show_id):

    form = ShowForm()
    show = Show.query.get(show_id)
    form.name.data = show.name
      
    return render_template("shows/details/new.html", show = show, form = form)

@app.route("/shows/details/update/<show_id>/", methods=["POST"])
@login_required(role="ADMIN")
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
    
    db.session().commit()
  
    return redirect(url_for("shows_index"))


@app.route("/workshift/<show_id>/", methods=["POST"])
@login_required
def shows_hand_up(show_id):

    # First check if user has already signed up for this show

    shiftExists = Shift.check_if_exists(current_user.id, show_id)

    # shiftExists is 0 if sign-up doesn't exist.

    if (shiftExists < 1):

        shift=Shift(current_user.id, show_id)
        db.session().add(shift)

        db.session.commit()

        shiftIdList = Shift.getShiftId(current_user.id, show_id)
        
        shiftdetails=ShiftDetails(shift_id=shiftIdList[0])
        db.session.add(shiftdetails)

        db.session().commit()

    

  
    return redirect(url_for("list_open_shows"))

@app.route("/shows/open_shows/", methods=["GET"])
@login_required
def list_open_shows():

    #shiftIds is fetched to determine in the template whether the current_user has signed up for the shows. It is a list of show id's.

    shiftIds = Shift.getShowIdsByUserId(current_user.id)

    return render_template("shows/open_shows/list.html", shows = Show.query.order_by(Show.show_date).all(), shiftIds=shiftIds)

@app.route("/shows/information/<show_id>/", methods=["GET"])
@login_required
def show_information(show_id):

    
    show = Show.query.get(show_id)
    
      
    return render_template("shows/information/showinfo.html", show = show)