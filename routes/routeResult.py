from flask import Blueprint, request, jsonify
from controllers.controllerResults import ControllerResults

result = Blueprint('result', __name__)
cont = ControllerResults()

#ADMINISTRACIÓN DE RESULTADOS.

@result.post("/result") #Método post para hacer el registro de un resultado
def create_results():
    data = request.get_json() #Se requiere el JSON con la información
    info = cont.create(data)
    return info[0], info[1]

@result.get("/result") #Método get para listar todas los resultados que están en la Base de datos.
def list_all_results():
    data = cont.index()
    return data[0], data[1]

@result.get("/result/<int:id>") #Método get para listar resultados dado un id
def results_by_id(id):
    data = cont.show(id)
    return data[0], data[1]

@result.put("/result/<int:id>") #Método put para editar un resultado dado un id y la info en un JSON
def put_result(id):
    data = request.get_json() #Se requiere el JSON con la información
    info = cont.update(id, data)
    return info[0], info[1]

@result.delete("/result/<int:id>") #Método delete para eliminar un resultado dado el parámetro id
def delete_result(id):
    data = cont.delete(id)
    return data[0], data[1]