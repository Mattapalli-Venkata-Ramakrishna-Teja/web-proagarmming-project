from datetime import datetime
from app import db


class  Addstock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tabname = db.Column(db.String(64), index=True, unique=True)
    company = db.Column(db.String(120), index=True, unique=True)
    doe=db.Column(db.Date)
    def __repr__(self):
        return '<Addstock {}>'.format(self.tabname)

class Addbuyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    amount=db.Column(db.Integer, index=True)
    status=db.Column(db.Boolean, index=True)
    date=db.Column(db.Date)

    def __repr__(self):
        return '<Addbuyer {}>'.format(self.name)
