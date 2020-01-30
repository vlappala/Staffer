from application import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.productions.models import Production
from application.productions.forms import ProductionForm

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
  