from application import db
from dateutil import parser

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    show_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    open_for_recruitment = db.Column(db.Boolean, nullable=False)

    production_id = db.Column(db.Integer, db.ForeignKey('production.id'),
                           nullable=False)

    # Konstruktorin kehitysversio:     def __init__(self, name, show_date):
    def __init__(self, name, show_date):
        self.name = name
        self.show_date = show_date
        # self.done = False
        self.open_for_recruitment = False

    @staticmethod
    def find_shows_with_most_job_openings():
        stmt = "SELECT production.id, production.name, COUNT(show.id) FROM production LEFT JOIN show ON show.production_id = production.id GROUP BY production.id"
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response

# class Production(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
#     onupdate=db.func.current_timestamp())

#     name = db.Column(db.String(144), nullable=False)

#     # Konstruktorin kehitysversio:     def __init__(self, name, show_date):
#     def __init__(self, name):
#         self.name = name

#         # self.done = False
