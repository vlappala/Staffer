from application import db

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    show_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    # done = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, show_date):
        self.name = name
        self.show_date = show_date
        # self.done = False