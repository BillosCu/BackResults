from flask import Blueprint, jsonify, request
from controllers.controllerPoliticanparty import ControllerPoliticanParty

politican = Blueprint('politican', __name__)

cont = ControllerPoliticanParty()

@politican.post("/pp")
def create_pp():
    data = request.get_json()
    info = cont.create(data)
    return info[0], info[1]

@politican.get("/pp")
def list_pp():
    data = cont.index()
    return data[0], data[1]

    
@politican.get("/pp/<int:id>")
def list_pp_by_id(id):
    data = cont.show(id)
    return data[0], data[1]


@politican.put("/pp/<int:id>")
def put_pp(id):
    data = request.get_json()
    info = cont.update(id, data)
    return info[0], info[1]

@politican.delete("/pp/<int:id>")
def delete_pp(id):
    data = cont.delete(id)
    return data[0], data[1]
