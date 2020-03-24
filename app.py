from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


from models.viajes import Viajes
from models.usuarios import Usuarios
from models.tipos_transportes import Tipos_Transportes


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emisiones.s3db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

db = SQLAlchemy()
db.init_app(app)



@app.route('/resumen',  methods = ['GET'])
def get_resumen():
    viajes = [item.serialize() for item in  Viajes.query.all()]
    return jsonify(viajes), 200

@app.route('/transporte',  methods = ['GET'])
def get_transp():
    transporte = [item.serialize() for item in Tipos_Transportes.query.all()]
    return jsonify(transporte), 200


@app.route('/agregar-viaje',  methods = ['POST'])
def post_viaje():
    viaje = Viajes()
    viaje.punto_partida = request.json.get('punto_partida')
    viaje.punto_termino = request.json.get('punto_termino')
    viaje.id_transporte = request.json.get('id_transporte')
    viaje.distancia_km = request.json.get('distancia_km')
    viaje.id_usuario = request.json.get('id_usuario')
    viaje.viaje_redondo = request.json.get('viaje_redondo')
    viaje.emision = get_emision(viaje.distancia_km, viaje.id_transporte, viaje.viaje_redondo)

    db.session.add(viaje)
    db.session.commit()

    return jsonify(viaje.serialize()), 201


def get_emision(distancia, id_transporte, viaje_redondo):
    transporte = Tipos_Transportes.query.filter_by(id = id_transporte).first()
    ida_vuelta = 2 if viaje_redondo else 1
    return float(distancia) * ida_vuelta * transporte.factor



if __name__ == '__main__':
    app.run()