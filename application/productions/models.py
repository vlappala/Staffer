from application import db
from dateutil import parser

class Production(db.Model):

    __tablename__ = "production"

    id = db.Column(db.Integer, primary_key=True)
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    show_duration_hours = db.Column(db.Integer, nullable=False)
    show_duration_minutes = db.Column(db.Integer, nullable=False)
    misc_info = db.Column(db.String(2000), nullable=True)

    shows = db.relationship("Show", backref='production', lazy=True)


    def __init__(self, name):
        self.name = name


