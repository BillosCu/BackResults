from db import db
from .results import Results

class Candidates(db.Model):
    __tablename__ = 'candidate'
    cedula = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String)
    last_name = db.Column(db.String)
    resolution = db.Column(db.String)
    id_politicanparty = db.Column(db.Integer, db.ForeignKey('politicanparty.id'))
    # table = db.relationship("Tables", backref=db.backref('candidate', lazy=True))
    # result = db.relationship("Results", secondary=Results, backref=db.backref('cant_votos', lazy=True))


    def __init__(self, cedula, name, last_name, resolution, id_politicanparty):
        self.cedula = cedula
        self.name = name
        self.last_name = last_name
        self.resolution = resolution
        self.id_politicanparty = id_politicanparty