from application import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.productions.models import Production
from application.productions.forms import ProductionForm

from application.shows.models import Show
from application.shows.forms import ShowForm

from dateutil import parser
from datetime import *

@app.route("/productions/new/")
@login_required
def productions_form():
    # wanha: return render_template("shows/new.html")
    return render_template("productions/new.html", form = ProductionForm())

@app.route("/productions/", methods=["POST"])
@login_required
def productions_create():

    form = ProductionForm(request.form)

    if not form.validate():
        return render_template("productions/new.html", form = form)


    s_name = form.name.data

    t = Production(s_name)


    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("productions_index"))

@app.route("/productions/", methods=["GET"])
@login_required
def productions_index():
    return render_template("productions/list.html", productions = Production.query.all())
  
@app.route("/productions/prodshows/<production_id>/", methods=["GET"])
@login_required
def add_shows_to_production(production_id):

    production = Production.query.get(production_id)

    # shows = Show.query.get(production_id)

    form = ShowForm()
 
  
    # return render_template("productions/askshows.html", shows=Show.query.get(production_id), form=form, production=production)

    return render_template("productions/askshows.html", form=form, production=production)

@app.route("/productions/prodshows/<production_id>/", methods=["POST"])
@login_required
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

    t.production_id = production.id

    db.session().add(t)
    db.session().commit()
  
    # return redirect(url_for("shows_index"))
 
  
    return redirect(url_for("productions_index"))