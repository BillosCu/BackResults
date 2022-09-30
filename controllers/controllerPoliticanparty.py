from models.politicanparty import PoliticanParty
from db import db
from flask import jsonify


class ControllerPoliticanParty():
    def __init__(self):
        pass

    def index(self):
        data = PoliticanParty.query.all()
        if(not data):
            return [{
                "mensaje": "No hay partidos políticos que listar"
            }, 200]
        array = []
        for i in data:
            info = {
                "id": i.id,
                "nombre": i.name,
                "lema": i.slogan
            }
            array.append(info)
        return [jsonify(array), 200]
    
    def create(self, data):
        flag = False
        if(not data['name']):
            return [{
                "error": "Requiere un nombre"
            }, 400]
        if(not data['slogan']):
            return [{
                "error": "Requiere un lema"
            }, 400]
        PP = PoliticanParty.query.all()
        for i in PP:
            if(i.name.lower() == data['name'].lower()):
                flag = True
        
        if(not flag):
            newPP = PoliticanParty(name=data['name'], slogan=data['slogan'])
            db.session.add(newPP)
            db.session.commit()
            return [{
                "id": newPP.id,
                "name": newPP.name,
                "slogan": newPP.slogan
            }, 201]
        else:
            return [{
                "error": "El partido político " + data['name'] + " ya existe"
            }, 400]

    
    def show(self, id):
        data = PoliticanParty.query.get(id)
        if(data == None):
            text = [{
                "error": "El partido político " + str(id) + " no registra."
            }, 400]
        else:
            text = [{
                "id": data.id,
                "nombre": data.name,
                "lema": data.slogan
            }, 200]
        return [jsonify(text[0]), text[1]]

    
    def update(self, id, data):
        info = PoliticanParty.query.get(id)
        if(info == None):
            text = [{
                "mensaje": "El id " + str(id) + " no existe"
            }, 400]
        else:
            if(not data['name']):
                return [{
                    "error": "Requiere un nombre"
                }, 400]
            if(not data['name']):
                return [{
                    "error": "Requiere un nombre"
                }, 400]
            info.name = data['name']
            info.slogan = data['slogan']
            db.session.add(info)
            db.session.commit()
            text = [{
                "mensaje": "se modificó el partido político con id " + str(id),
                "name": info.name,
                "slogan": info.slogan
            }, 200]
        return [jsonify(text[0]), text[1]]
    

    def delete(self, id):
        info = PoliticanParty.query.get(id)
        oldId = id
        if (info == None):
            text =[{
                "mensaje": "El partido político con id " + str(id) + " no está en la base de datos"
            }, 400]
        else:
            db.session.delete(info)
            db.session.commit()
            text =[{
                "id": oldId,
                "mensaje": "eliminado correctamente"
            }, 200]
        return [jsonify(text[0]), text[1]]