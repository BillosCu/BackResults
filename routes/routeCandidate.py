from flask import Blueprint, request
from controllers.controllerCandidates import ControllerCandidates

candidate = Blueprint('candidate', __name__)


cont = ControllerCandidates()


@candidate.post("/candidate")
def create_candidate():
    data = request.get_json()
    info = cont.create(data)
    return info[0], info[1]

@candidate.get("/candidate")
def list_candidates():
    data = cont.index()
    return data[0], data[1]

@candidate.get("/candidate/<int:id>")
def list_candidate_by_id(id):
    data = cont.show(id)
    return data[0], data[1]

@candidate.put("/candidate/<int:id>")
def put_candidate(id):
    data = request.get_json()
    info = cont.update(id, data)
    return info[0], info[1]

@candidate.delete("/candidate/<int:id>")
def delete_candidate(id):
    data = cont.delete(id)
    return data[0], data[1]