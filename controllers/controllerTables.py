from models.results import Results
from models.tables import Tables
from models.candidates import Candidates
from models.politicanparty import PoliticanParty
from db import db
from flask import jsonify


class ControllerTables():
    def __init__(self):
        pass

    def index(self):
        data = Tables.query.all() #Data me trae de la base de datos toda la información de la tabla "mesas"
        if(not data):
            return [{
                "mensaje": "No hay mesas que listar"
            }, 200]
        array = [] #inicializamos un arreglo vacio para ir guardando la información
        for i in data:
            info = {
                "id": i.id,
                "cant_cedulas": i.cant_cedulas
            }
            array.append(info)
        return [jsonify(array), 200]


    def create(self, data):
        if(not data['cant_cedulas']):
            return [{
                "error": "Requiere una cantidad de cédulas"
            }, 400]
        newTable = Tables(cant_cedulas=data['cant_cedulas'])
        db.session.add(newTable)
        db.session.commit()
        return [{
            "id": newTable.id,
            "cant_cedulas": newTable.cant_cedulas
        }, 201]


    def show(self, id):
        table = Tables.query.get(id) #Me trae la información de una sola mesa con el id dado.
        if(table == None):
            text = [{
                "error": "La mesa con id " + str(id) + " no registra." #Si no encuentra la mesa, envía este error.
            }, 400]
        else:
            text = [{
                "id": table.id,
                "cedulas": table.cant_cedulas
            }, 200]
        return [jsonify(text[0]), text[1]]


    def update(self, id, data):
        tableInfo = Tables.query.get(id) 
        if (tableInfo == None):
            text =[{
                "mensaje": "El id " + str(id) + " no existe"
            }, 400]
        else:
            if(not data['cant_cedulas']):
                return [{
                    "error": "Requiere una cantidad de cédulas"
                }, 400]
            before = tableInfo.cant_cedulas
            tableInfo.cant_cedulas = data['cant_cedulas']
            db.session.add(tableInfo)
            db.session.commit()
            text = [{
                "mensaje": "se modificó la mesa con id " + str(id),
                "cedulas_antes": before,
                "nuevas_cedulas": tableInfo.cant_cedulas
            }, 200]
        return [jsonify(text[0]), text[1]]
    

    def delete(self, id):
        tableInfo = Tables.query.get(id)
        oldId = id
        if (tableInfo == None):
            text =[{
                "mensaje": "la mesa con id " + str(id) + " no está en la base de datos"
            }, 400]
        else:
            db.session.delete(tableInfo)
            db.session.commit()
            text =[{
                "id": oldId,
                "mensaje": "eliminado correctamente"
            }, 200]
        return [jsonify(text[0]), text[1]]



    def reportVotesCandidate(self, id_table, id_candidate):
        table = Tables.query.get(id_table)
        candidate = Candidates.query.get(id_candidate)
        result = Results.query.filter(id_candidate=id_candidate)

        if result.cant_votos != 0:
            text = [{
                "Partido": candidate.id_politicanparty.name,
                "Candidato": candidate.name + " " + candidate.last_name,
                "Mesa": table.id,
                "Votos": result.cant_votos
            }, 200]
        else:
            text = [{
                "mensaje": "el candidato " + candidate.name + " " + candidate.last_name + " no tiene votos."
            }, 200]
        return [jsonify(text[0]), text[1]]



    # def reportVotesPoliticanParty(self, id_table, id_party):
    #     table = Tables.query.get(id_table)
    #     party = PoliticanParty.query.get(id_party)

    #     if 








