from db import db

class Tables(db.Model):
    __tablename__ = 'table'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cant_cedulas = db.Column(db.Integer)

    def __init__(self, cant_cedulas):
        self.cant_cedulas = cant_cedulas