from models.candidates import Candidates
from models.politicanparty import PoliticanParty
from db import db
from flask import jsonify

class ControllerCandidates():
    def __init__(self):
        pass

    def index(self):
        data = Candidates.query.all()#Data me trae de la base de datos toda la información de la tabla "candidatos"
        if(not data):
            return [{
                "mensaje": "No hay candidatos que listar"
            }, 200]
        array = []
        for i in data:
            idPP = i.id_politicanparty
            infoPP = PoliticanParty.query.get(idPP)
            info = {
                "cedula": i.cedula,
                "nombre": i.name,
                "last_name": i.last_name,
                "resolution": i.resolution,
                "politicanparty": infoPP.name
            }
            array.append(info)
        return [jsonify(array), 200]


    def create(self, data):
        flag = False
        name=None
        last_name = None
        pp = None
        resolution=None
        cedula = None
        allCand = Candidates.query.all()
        if data: 
            for key, val in data.items():
                if key == 'cedula' and type(val) == int:
                    cand = Candidates.query.get(data['cedula'])
                    cedula = data['cedula']
                if key == 'name' and type(val) == str:
                    name = data['name']
                if key == 'last_name' and type(val) == str:
                    last_name = data['last_name']
                if key == 'resolution' and type(val) == str:
                    resolution = data['resolution']
                if key == 'id_politicanparty' and type(val) == int:
                    pp = data['id_politicanparty']

            if cedula == None:
                return [{
                    "error": "se requiere la cédula."
                }, 400]

            if name == None or last_name == None:
                return [{
                    "error": "se requiere el nombre y el apellido"
                }, 400]

            if resolution == None:
                return [{
                    "error": "se requiere la resolución."
                }, 400]

            for i in allCand:
                if i.resolution == resolution:
                    flag = True

            if flag:
                return [{
                    "error": "la resolución ya existe."
                }, 400]

            if pp == None:
                return [{
                    "error": "se requiere un partido político."
                }, 400]

            if cand != None:
                return[{
                    "error": "el usuario ya existe"
                }, 400]
            else:
                party = PoliticanParty.query.get(pp)
                newCandidate = Candidates(cedula=cedula, name=name, last_name=last_name, resolution=resolution, id_politicanparty=pp) 
                db.session.add(newCandidate)
                db.session.commit()
                return [{
                    "cedula": cedula,
                    "name": name,
                    "last_name": last_name,
                    "resolution": resolution,
                    "politicanparty": party.name
                }, 201]        
            

    def show(self, id):
        info = Candidates.query.get(id)
        if (info == None):
            text = [{
                "error": "el candidato con id " + str(id) + " no registra."
            }, 400]
        else:
            pp = PoliticanParty.query.get(info.id_politicanparty)
            text = [{
                "cedula": info.cedula,
                "nombre": info.name,
                "last_name": info.last_name,
                "resolution": info.resolution,
                "politicanparty": pp.name
            }, 200]
        return [jsonify(text[0]), text[1]]

    def update(self, id, data):
        info = Candidates.query.get(id)
        if (info == None):
            text = [{
                "mensaje": "El id " + str(id) + " no existe"
            }, 400]
        else:
            if(not data['name']):
                return [{
                    "error": "Requiere un nombre"
                }, 400]
            if(not data['last_name']):
                return[{
                    "error": "Requiere el apellido"
                }, 400]
            oldName = info.name
            oldLastName = info.last_name
            info.name = data['name']
            info.last_name = data['last_name']
            db.session.add(info)
            db.session.commit()
            text = [{
                "mensaje": "se modificó *" + oldName + " " + oldLastName + "* a *" + info.name + " " + info.last_name + "*"
            }, 200]
        return [jsonify(text[0]), text[1]]

    

    def delete(self, id):
        data = Candidates.query.get(id)
        oldId = id
        if(data == None):
            text =[{
                "mensaje": "El candidado con id " + str(id) + " no está en la base de datos"
            }, 400]
        else:
            db.session.delete(data)
            db.session.commit()
            text =[{
                "mensaje": "candidado con id "+ str(oldId) + " eliminado"
            }, 200]
        return (jsonify(text[0]), text[1])

