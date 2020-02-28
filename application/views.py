from flask import render_template

from flask_login import current_user

from application import app, db
from application.shows.models import Show
from application.auth.models import User
from application.workshift.models import Shift

from application.roles.models import Role

@app.route("/")
def index():

    users = User.query.all()

    showList = []

    if current_user.is_authenticated:


        shiftsFromDb = Shift.getShowIdsByUserId(current_user.id)



        if (len(shiftsFromDb) > 0):
        
            for shift in shiftsFromDb:
                show = Show.query.get(shift)
                print(show.name)
                showList.append(show)

    return render_template("index.html", most_openings=Show.find_shows_with_most_job_openings(), users=users, showList=showList, usersWithShifts=Shift.find_users_with_most_shifts())





