from models.candidates import Candidates
from models.tables import Tables
from models.results import Results
from db import db
from flask import jsonify

class ControllerResults():
    def __init__(self):
        pass

    def index(self):
        data = Results.query.all()
        if(not data):
            return [{
                "mensaje": "No hay resultos que listar"
            }, 200]
        arr = []
        for i in data:
            info = {
                "id": i.id,
                "id_candidate": i.id_candidate,
                "id_table": i.id_table,
                "cant_votos": i.cant_votos
            }
            arr.append(info)
        return [jsonify(arr), 200]

    def create(self, data):
        flag = False
        id_candidate = data['id_candidate']
        id_table = data['id_table']
        cant_votos = data['cant_votos']
        cand = Candidates.query.get(id_candidate)
        tab = Tables.query.get(id_table)
        result = Results.query.all()
        if(cand == None and tab == None):
            return [{
                "error": "Ni el candidato, ni la mesa existen"
            }, 404]
        if(tab == None):
            return [{
                "error": "La mesa no existe"
            }, 404]
        if(cand == None):
            return [{
                "error": "El candidato no existe"
            }, 404]
        if(tab.cant_cedulas < cant_votos):
            text =[{
                "error": "Cantidad de votos incorrecta"
            }, 400]
        else:
            if (result == []):
                newResult = Results(id_candidate = id_candidate, id_table=id_table, cant_votos=cant_votos)
                db.session.add(newResult)
                db.session.commit()
                return [{
                    "id": newResult.id,
                    "id_candidate": id_candidate,
                    "id_table": id_table,
                    "cant_votos": cant_votos
                }, 201]
            else:
                for i in result:
                    if(cand.cedula == i.id_candidate and tab.id == i.id_table):
                        flag = True
                if(flag == False):
                    print("entre")
                    newResult = Results(id_candidate = id_candidate, id_table=id_table, cant_votos=cant_votos)
                    db.session.add(newResult)
                    db.session.commit()
                    return [{
                        "id": newResult.id,
                        "id_candidate": id_candidate,
                        "id_table": id_table,
                        "cant_votos": cant_votos
                    }, 201]  
                else:
                    text = [{
                        "Mensaje": "El candidato ya tiene votos registrados."
                    }, 400]
        return [jsonify(text[0]), text[1]]

    def show(self, id):
        data = Results.query.get(id)
        if(data == None):
            text = [{
                "error": "El resultado " + str(id) + " no registra."
            }, 404]
        else:
            text = [{
                "id": data.id,
                "id_candidate": data.id_candidate,
                "id_table": data.id_table,
                "cant_votos": data.cant_votos
            }, 200]
        return [jsonify(text[0]), text[1]]

    def update(self, id, data):
        info = Results.query.get(id)
        if(info == None):
            text = [{
                "mensaje": "El id " + str(id) + " no existe"
            }, 404]
        else:
            if(not data['cant_votos']):
                return [{
                    "error": "Requiere una cantidad de cédulas"
                }, 400]
            info.cant_votos = data['cant_votos']
            db.session.add(info)
            db.session.commit()
            text = [{
                "mensaje": "se modificó el resultado con id " + str(id)
            }, 200]
        return [jsonify(text[0]), text[1]]

    def delete(self, id):
        info = Results.query.get(id)
        oldId = id
        if(info == None):
            text = [{
                "mensaje": "El resultado con id " + str(id) + " no existe"
            }, 404]
        else:
            db.session.delete(info)
            db.session.commit()
            text = [{
                "mensaje": "El resultado con id " + str(oldId) + " se eliminó"
            }, 200]
        return [jsonify(text[0]), text[1]]


    def updateCandidateVotes(self, id_table, id_candidate, votos):
        table = Tables.query.get(id_table)
        candidate = Candidates.query.get(id_candidate)
        if votos <= table.cant_cedulas and votos >= 0:
            candidate.result += candidate.result + votos
            db.session.add(candidate)
            db.session.commit()
            text = [{
                "mensaje": "se modificaron los votos del candidato " + candidate.name + " " + candidate.last_name
            }, 200]
        else:
            text =[{
                "mensaje": "No se puede modificar con los datos ingresados"
            }, 200]

        return [jsonify(text[0]), text[1]]