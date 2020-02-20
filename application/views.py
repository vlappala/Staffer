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

    shifts = []

    if current_user.is_authenticated:
        print()
        print("FOO")
        print()

        shiftsFromDb = Shift.getShowIdsByUserId(current_user.id)

        


        print()

        # print(Role.getRoleByUserId(current_user.id))

        # roles = Role.getRoleByUserId(current_user.id)

        #for role in roles:
        #    print(role)

        print()

        if (len(shiftsFromDb) > 0):
        
            for shift in shiftsFromDb:
                show = Show.query.get(shift)
                print(show.name)
                shifts.append(show)

    return render_template("index.html", most_openings=Show.find_shows_with_most_job_openings(), users=users, shifts=shifts)





