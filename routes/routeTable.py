from flask import Blueprint, request
from controllers.controllerTables import ControllerTables


table = Blueprint('table', __name__)

cont = ControllerTables()
#ADMINISTRACIÓN DE MESAS

@table.post("/table") #Método post para hacer el registro de una mesa
def create_tables():
    data = request.get_json() #Se requiere el JSON con la información
    info = cont.create(data)
    return info[0], info[1]


@table.get("/table") #Método get para listar todas las mesas que están en la Base de datos.
def list_tables():
    data = cont.index()
    return data[0], data[1]

@table.get("/table/<int:id>") #Método get para listar las mesas dado un id
def table_by_id(id):
    data = cont.show(id)
    return data[0], data[1]

@table.put("/table/<int:id>") #Método put para editar una mesa dado un id y la info en un JSON
def put_table(id):
    data = request.get_json() #Se requiere el JSON con la información
    info = cont.update(id, data)
    return info[0], info[1]


@table.delete("/table/<int:id>") #Método delete para eliminar una mesa dado el parámetro id
def delete_table(id):
    data = cont.delete(id)
    return data[0], data[1]