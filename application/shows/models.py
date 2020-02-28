from application import db
from dateutil import parser

from sqlalchemy.sql import text

class Show(db.Model):

    __tablename__ = "show"

    id = db.Column(db.Integer, primary_key=True)
    show_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    

    production_id = db.Column(db.Integer, db.ForeignKey('production.id'),
                           nullable=False)

    shifts = db.relationship("Shift", backref='show', lazy=True)


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



    @staticmethod
    def production_name_has_changed(production_id, new_name):
        stmt = text("UPDATE show SET name = :name WHERE production_id = :pr_id").params(pr_id=production_id, name=new_name)
        res = db.engine.execute(stmt)
  
    
    @staticmethod
    def getShowIdsByProductionId(production_id):
        stmt = text("SELECT id FROM show WHERE production_id = :pr_id;").params(pr_id=production_id)
        res = db.engine.execute(stmt)

        
  
        response = []
        for row in res:



            response.append(row[0])

        return response

