from application import db
from dateutil import parser

from sqlalchemy.sql import text

class Role(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    role_name = db.Column(db.String(144), nullable=False)
    
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())


    def __init__(self, account_id, role_name):
        self.account_id = account_id
        self.role_name = role_name

    @staticmethod
    def getRoleByUserId(account_id):
        stmt = text("SELECT role.role_name FROM role WHERE role.account_id = :ac_id").params(ac_id=account_id)
        res = db.engine.execute(stmt)

        
        response = []
  
        
        if res is not None:

            for row in res:
                
                # return row[0]
                
                response.append(row[0])
                # print()
                # print(row[0])
                # print()
                
        
        return response

