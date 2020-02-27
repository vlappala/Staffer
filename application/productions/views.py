from application import app, db, login_required

from flask import redirect, render_template, request, url_for
# from flask_login import login_required

from application.productions.models import Production
from application.productions.forms import ProductionForm

from application.shows.models import Show
from application.shows.forms import ShowForm

from application.workshift.models import Shift, ShiftDetails

from dateutil import parser
from datetime import *

from datetime import datetime

@app.route("/productions/new/")
@login_required(role="ADMIN")
def productions_form():

    return render_template("productions/new.html", form = ProductionForm())

@app.route("/productions/", methods=["POST"])
@login_required(role="ADMIN")
def productions_create():

    form = ProductionForm(request.form)

    if not form.validate():
        return render_template("productions/new.html", form = form)


    production_name = form.name.data

    # testitulostusta, tyyppi on: datetime.time:
    print(str(form.show_duration.data))
    print("Tyyppiä: ", type(form.show_duration.data))

    production = Production(production_name)
    production.misc_info = form.misc_info.data

    # showduration =  ""
    # showduration = showduration + form.show_duration.data.strftime("%H:%M")

    # showduration = parser.parse(showduration)

    print(form.show_duration.data.hour)

    production.show_duration_hours = int(form.show_duration.data.hour)
    production.show_duration_minutes = int(form.show_duration.data.minute)


    db.session().add(production)
    db.session().commit()
  
    return redirect(url_for("productions_index"))

@app.route("/productions/", methods=["GET"])
@login_required(role="ADMIN")
def productions_index():
    return render_template("productions/list.html", productions = Production.query.all())
  
@app.route("/productions/prodshows/<production_id>/", methods=["GET"])
@login_required(role="ADMIN")
def add_shows_to_production(production_id):

    production = Production.query.get(production_id)

    # shows = Show.query.get(production_id)

    form = ShowForm()
 
  
    # return render_template("productions/askshows.html", shows=Show.query.get(production_id), form=form, production=production)

    return render_template("productions/askshows.html", form=form, production=production)

@app.route("/productions/prodshows/<production_id>/", methods=["POST"])
@login_required(role="ADMIN")
def post_shows_to_production(production_id):

    production = Production.query.get(production_id)

    form = ShowForm(request.form)

    form.name.data = production.name

    if not form.validate():
        return render_template("productions/askshows.html", form=form, production=production)


    s_name = form.name.data
    showtime = ""
    showtime = showtime + form.showdate.data.strftime("%Y-%m-%d")
    showtime = showtime + " "
    showtime = showtime + form.showtime.data.strftime("%H:%M")
    showtime = parser.parse(showtime)


    show = Show(s_name, showtime)



    show.production_id = production.id

    db.session().add(show)
    db.session().commit()
  

 
  
    return redirect(url_for("productions_index"))

@app.route("/productions/details/<production_id>/", methods=["GET"])
@login_required(role="ADMIN")
def production_details(production_id):

    form = ProductionForm()
    production = Production.query.get(production_id)

    form.name.data = production.name
    form.misc_info.data = production.misc_info

    string_time = ''
    string_time = string_time + str(production.show_duration_hours)
    string_time = string_time + ':'
    string_time = string_time + str(production.show_duration_minutes)

    print()
    print(string_time)
    print()

    form_time = datetime.strptime(string_time, '%H:%M').time()

    form.show_duration.data = form_time
    # form.show_duration.data.minute = int(production.show_duration_minutes)

    # int(form.show_duration.data.hour)

    
    return render_template("productions/details/new.html", production = production, form = form)

@app.route("/productions/details/update/<production_id>/", methods=["POST"])
@login_required(role="ADMIN")
def production_update(production_id):

    form = ProductionForm(request.form)


    if not form.validate():
        return render_template("productions/details/new.html", form = form)

    production = Production.query.get(production_id)
    production.name = form.name.data

    # testitulostusta, tyyppi on: datetime.time:
    print(str(form.show_duration.data))
    print("Tyyppiä: ", type(form.show_duration.data))

    # production = Production(production_name)
    production.misc_info = form.misc_info.data

    # showduration =  ""
    # showduration = showduration + form.show_duration.data.strftime("%H:%M")

    # showduration = parser.parse(showduration)

    print(form.show_duration.data.hour)

    production.show_duration_hours = int(form.show_duration.data.hour)
    production.show_duration_minutes = int(form.show_duration.data.minute)


    db.session().commit()

    Show.production_name_has_changed(production.id, form.name.data)
  

    return redirect(url_for("productions_index"))


@app.route("/productions/delete/<production_id>/", methods=["POST"])
@login_required(role="ADMIN")
def production_delete(production_id):

    showIdList = Show.getShowIdsByProductionId(production_id)

    if showIdList is not None:

        for showId in showIdList:

            shiftIds = Shift.find_shiftIds_by_showId(showId)

            for shiftId in shiftIds:
        
                shiftdetails = ShiftDetails.query.get(shiftId)
                db.session.delete(shiftdetails)
                db.session.commit()

                shift = Shift.query.get(shiftId)
                db.session.delete(shift)
                db.session.commit()
        
            
    if showIdList is not None:

        for showId in showIdList:    
            
            show = Show.query.get(showId)

            db.session.delete(show)
            db.session.commit()

    production = Production.query.get(production_id)
    db.session.delete(production)
    
    
    db.session().commit()
  
    return redirect(url_for("productions_index"))