from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from models.viajes import Viajes
from models.usuarios import Usuarios
from models.viajes import Viajes



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emisiones.s3db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)



@app.route('/resumen',  methods = ['GET'])
def get_resumen():
    viajes = [item.serialize() for item in  Viajes.query.all()]
    return jsonify(viajes), 200


@app.route('/agregar-viaje',  methods = ['POST'])
def post_viaje():
    viaje = Viajes()
    viaje.punto_partida = request.json.get('punto_partida')
    viaje.punto_termino = request.json.get('punto_termino')
    viaje.id_transporte = request.json.get('id_transporte')
    viaje.distancia_km = request.json.get('distancia_km')
    viaje.id_usuario = request.json.get('id_usuario')
    viaje.viaje_redondo = True
    viaje.emision = 0  

    print("Paso1")

    db.session.add(viaje)
    db.session.commit()

    return jsonify(viaje.serialize()), 201

if __name__ == '__main__':
    app.run()