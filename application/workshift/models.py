from application import db
from dateutil import parser

from sqlalchemy.sql import text

from sqlalchemy import UniqueConstraint

class Shift(db.Model):

    __tablename__ = "shift"

    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'),
                           nullable=False)
    shift_role = db.Column(db.String(144), nullable=True)
    shift_locked = db.Column(db.Boolean, nullable=False, default=False)
    shift_completed = db.Column(db.Boolean, nullable=False, default=False)
    shift_billed = db.Column(db.Boolean, nullable=False, default=False)

    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    __table_args__ = (
        UniqueConstraint("account_id", "show_id"),
    )

    

    
    def __init__(self, account_id, show_id):
        self.account_id = account_id
        self.show_id = show_id

    
    @staticmethod
    def find_shifts_with_sign_ups():
        stmt = text("SELECT show.name, show.show_date, shift.show_id, count(shift.show_id) AS LKM FROM shift, show where show.id = shift.show_id GROUP BY show.name ORDER BY LKM DESC;")
        
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"LKM":row[3], "show_id":row[2], "name":row[0], "date":row[1]})

        return response

        def __init__(self, account_id, show_id):
            self.account_id = account_id
            self.show_id = show_id

    



    # Checks if announcement already exists

    @staticmethod
    def get_instance(account_id, show_id):
        stmt = text("SELECT shift.id FROM shift WHERE shift.account_id = :ac_id AND shift.show_id = :s_id").params(ac_id=account_id, s_id=show_id)
        res = db.engine.execute(stmt)

        palautus = 0
        response = []
  
        
        if res is not None:
            print()
            print("TRUE")
            print(res)
            print()

            for row in res:
                palautus = palautus + 1
                response.append(row[0])
                print("Vuoron Id: ", row[0])
        print(palautus)
        return len(response)


        
    @staticmethod
    def getShowIdsByUserId(account_id):
        stmt = text("SELECT shift.show_id FROM shift WHERE shift.account_id = :ac_id").params(ac_id=account_id)
        res = db.engine.execute(stmt)

        palautus = 0
        response = []
  
        
        if res is not None:
            print()
            print("TRUE")
            print(res)
            print()

            for row in res:
                palautus = palautus + 1
                response.append(row[0])
                print("Ilmoittautumisen vuoron id: ", row[0])
        print(palautus)
        return response


        