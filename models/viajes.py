import sqlite3
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Viajes(db.Model):
    __tablename__ = 'viajes'
    __table_args__ = { 'extend_existing': True }

    id = db.Column(db.Integer, primary_key=True)
    punto_partida = db.Column(db.String(100), nullable=False)
    punto_termino = db.Column(db.String(100), nullable=False)
    id_transporte = db.Column(db.Integer, nullable=False)
    distancia_km = db.Column(db.Float, nullable=False)
    id_usuario = db.Column(db.Integer, nullable=False)
    viaje_redondo = db.Column(db.Boolean, nullable=False)
    emision = db.Column(db.Float, nullable=False)

    
    def serialize(self):
        return {
            'punto_partida': self.punto_partida,
            'punto_termino': self.punto_termino,
            'id_transporte': self.id_transporte,
            'distancia_km': self.distancia_km,
            'id_usuario': self.id_usuario,
            'viaje_redondo': self.viaje_redondo,
            'emision': self.emision
        }
