from db import db

class PoliticanParty(db.Model):
    __tablename__ = 'politicanparty'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), unique=True)
    slogan = db.Column(db.String(255))


    def __inti__(self, name, slogan):
        self.name = name
        self.slogan = slogan