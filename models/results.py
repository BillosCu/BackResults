from db import db

class Results(db.Model):
    __tablename__ = 'result'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_candidate = db.Column(db.Integer, db.ForeignKey('candidate.cedula'))
    id_table = db.Column(db.Integer, db.ForeignKey('table.id'))
    cant_votos = db.Column(db.Integer)


    def __inti__(self, id_candidate, id_table, cant_votos):
        self.cant_votos = cant_votos
        self.id_candidate = id_candidate
        self.id_table = id_table