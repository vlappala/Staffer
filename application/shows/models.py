from application import db
from dateutil import parser

from sqlalchemy.sql import text

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    show_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    

    production_id = db.Column(db.Integer, db.ForeignKey('production.id'),
                           nullable=False)


    def __init__(self, name, show_date):
        self.name = name
        self.show_date = show_date


    @staticmethod
    def find_shows_with_most_job_openings():
        stmt = text("SELECT production.id, production.name, COUNT(show.id) AS LKM FROM production LEFT JOIN show ON show.production_id = production.id group by production.id ORDER BY LKM DESC;")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"LKM":row[2], "name":row[1]})

        return response

    @staticmethod
    def find_basic_show_info():
        stmt = text("SELECT name, show_date, open_for_recruitment, id FROM show ORDER BY show_date;")
        res = db.engine.execute(stmt)

        
  
        response = []
        for row in res:



            response.append({"show_date":row[1], "name":row[0], "open_for_recruitment":row[2], "id":row[3]})

        return response




