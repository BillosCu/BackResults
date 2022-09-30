from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from waitress import serve
import json
from routes.routeTable import table
from routes.routePoliticanParty import politican
from routes.routeCandidate import candidate
from routes.routeResult import result
from db import db

#Se instancia la aplicación.
app = Flask(__name__)
CORS(app)
#Cargamos el archivo con la configuración del URL y el puerto a usar.
def fileConfig():
    with open('config.json') as file:
        data = json.load(file)
    return data


dataConfig = fileConfig()

#Conexión a la Base de Datos.
conexionDB = "postgresql://" + dataConfig['userdb'] + ":" + dataConfig['passworddb'] + "@" + dataConfig['hostdb'] + ":5432/" + dataConfig['namedb'] 
app.config['SQLALCHEMY_DATABASE_URI'] = conexionDB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)

@app.get("/")
def index():
    return "index", 200

#Se hace el registro de los Blueprint para el acceso a las rutas.
app.register_blueprint(table)
app.register_blueprint(politican)
app.register_blueprint(candidate)
app.register_blueprint(result)




#Se hace la creación de las tablas en la base de datos.
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    print("Corriendo en http://" + dataConfig['url'] + ":" + str(dataConfig['port']) )
    serve(app, host=dataConfig['url'], port=dataConfig['port'])
    #app.run(debug=True)