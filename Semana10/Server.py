

import os #modulo de python, abstraccion del sistema operativo

from flask import Flask, jsonify, request #que es json??????
app = Flask(__name__) #constructor de Flask
app.debug = True #propiedad del objeto de Flask
persons = []#lista vacia

def id_exists(id, persons):
    app.logger.debug("id_exists was called")
    app.logger.debug(id)
    app.logger.debug(persons)
    for person in persons:
        if person["id"] == id:
            return True
    return False

@app.route('/') #decorador
def get_root_resource():
    return 'This is a root resource'

@app.route('/api/v1/person', methods=["POST"])
def post_person():
    #esto es una validacion para garantizar que los datos vienen en json que es
    #lo que este servidor sabe interpretar
    if not request.is_json(): #metodo, verdadero o falso, los datos vienen como json
        return jsonify({
            "msg": "Only json is supported in this API"
        }), 400


#Si llegamos aca es porque los datos si son JSON
datos = request.get_json()
#requisito: que tenga una llave que se llame id y que no este ya ahi

#para poder crear una persona (recurso), es mandatorio
#que tenga un id unico

if "id" not in datos:
    return jsonify({
        "msg": "An id is required"
    }), 400

    if id_exists(datos["id"], persons):
        return jsonify({
            "msg": "The provided id is already in use"
        }), 400

persons.append(datos)

return jsonify({
    "msg": "Person created"
}), 201

@app.route('/api/v1/person', methods=["GET"]) #methids recibe un array con strings, recibe el verbo http que yo quiero mappear
def get_person():
    return jsonify(persons), 200

if __name__ == "__main__": #solo si el archivo esta siendo ejecutado directamente
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)#metodo, por el punto, implica que se esta ejecutando una accion (run) sobre un objeto