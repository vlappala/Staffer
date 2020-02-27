from application import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.shows.models import Show
from application.shows.forms import ShowForm

from application.workshift.models import Shift, ShiftDetails

from dateutil import parser
from datetime import *



@app.route("/shifts/delete/<show_id>/", methods=["POST"])
@login_required
def shift_delete(show_id):

    # This method is used from the Main menu -page
    # Method deletes only those shifts that belong to the current user

    shiftIdAsList = Shift.getShiftId(current_user.id, show_id)

    

    
        
    shiftdetails = ShiftDetails.query.get(shiftIdAsList[0])
    db.session.delete(shiftdetails)
    db.session.commit()

    shift = Shift.query.get(shiftIdAsList[0])
    db.session.delete(shift)
    db.session.commit()

  
    return redirect(url_for("index"))

@app.route("/shifts/list_delete/<show_id>/", methods=["POST"])
@login_required
def shift_list_delete(show_id):

    # This method is used from List open shows -page
    # Method deletes only those shifts that belong to the current user

    shiftIdAsList = Shift.getShiftId(current_user.id, show_id)

    

    
        
    shiftdetails = ShiftDetails.query.get(shiftIdAsList[0])
    db.session.delete(shiftdetails)
    db.session.commit()

    shift = Shift.query.get(shiftIdAsList[0])
    db.session.delete(shift)
    db.session.commit()

  
    return redirect(url_for("list_open_shows"))

