from application import db
from dateutil import parser

class Production(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)

    # Konstruktorin kehitysversio:     def __init__(self, name, show_date):
    def __init__(self, name):
        self.name = name

        # self.done = False
