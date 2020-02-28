from application import db
from dateutil import parser

from sqlalchemy.sql import text

from sqlalchemy import UniqueConstraint

from datetime import datetime

class Shift(db.Model):

    __tablename__ = "shift"

    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'),
                           nullable=False)


    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    __table_args__ = (
        UniqueConstraint("account_id", "show_id"),
    )

    

    
    def __init__(self, account_id, show_id):
        self.account_id = account_id
        self.show_id = show_id


    @staticmethod
    def find_shiftIds_by_showId(show_id):
        stmt = text("SELECT shift.id FROM shift where show_id = :sh_id").params(sh_id=show_id)
        
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append(row[0])

        return response

  

    
    @staticmethod
    def find_shifts_with_sign_ups():
        stmt = text("SELECT show.name, show.show_date, shift.show_id, count(shift.show_id) AS LKM FROM shift, show where show.id = shift.show_id GROUP BY show.name, show.show_date, shift.show_id ORDER BY LKM DESC;")
        
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"LKM":row[3], "show_id":row[2], "name":row[0], "date":row[1]})

        return response

  


    @staticmethod
    def getShiftId(account_id, show_id):
        stmt = text("SELECT shift.id FROM shift WHERE shift.account_id = :ac_id AND shift.show_id = :s_id").params(ac_id=account_id, s_id=show_id)
        res = db.engine.execute(stmt)

        
        response = []

        if res is not None:

            for row in res:

                response.append(row[0])

        return response



    # Checks if announcement already exists

    @staticmethod
    def check_if_exists(account_id, show_id):
        stmt = text("SELECT shift.id FROM shift WHERE shift.account_id = :ac_id AND shift.show_id = :s_id").params(ac_id=account_id, s_id=show_id)
        res = db.engine.execute(stmt)

        
        response = []
  
        
        if res is not None:

            for row in res:

                response.append(row[0])

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

    @staticmethod
    def find_users_with_most_shifts():
        stmt = text("SELECT account.name, COUNT(shift.id) AS LKM FROM account LEFT JOIN shift ON account.id = shift.account_id group by account.name ORDER BY LKM DESC;")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"LKM":row[1], "name":row[0]})

        return response


class ShiftDetails(db.Model):

    __tablename__ = "shiftdetails"

    id = db.Column(db.Integer, primary_key=True)
    shift_id = db.Column(db.Integer, db.ForeignKey('shift.id'),
                           nullable=False)

    shift_role = db.Column(db.String(144), nullable=True, default=None)
    shift_locked = db.Column(db.Boolean, nullable=False, default=False)
    shift_completed = db.Column(db.Boolean, nullable=False, default=False)
    shift_billed = db.Column(db.Boolean, nullable=False, default=False)

    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())


    def __init__(self, shift_id):
        
        self.shift_id = shift_id




   