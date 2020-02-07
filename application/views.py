from flask import render_template
from application import app
from application.shows.models import Show

@app.route("/")
def index():
    return render_template("index.html", most_openings=Show.find_shows_with_most_job_openings())
