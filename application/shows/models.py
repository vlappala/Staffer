from application import db
from dateutil import parser

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    show_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    open_for_recruitment = db.Column(db.Boolean, nullable=False)

    # Konstruktorin kehitysversio:     def __init__(self, name, show_date):
    def __init__(self, name, show_date):
        self.name = name
        self.show_date = show_date
        # self.done = False
        self.open_for_recruitment = False

# class Production(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
#     onupdate=db.func.current_timestamp())

#     name = db.Column(db.String(144), nullable=False)

#     # Konstruktorin kehitysversio:     def __init__(self, name, show_date):
#     def __init__(self, name):
#         self.name = name

#         # self.done = False
