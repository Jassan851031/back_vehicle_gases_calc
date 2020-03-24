import sqlite3
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tipos_Transportes(db.Model):
    __tablename__ = 'tipos_transportes'
    __table_args__ = { 'extend_existing': True }

    id = db.Column(db.Integer, primary_key=True)
    transporte = db.Column(db.String(100), nullable=False)
    factor = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Tipos_Transportes %r>' % self.name
    
    def serialize(self):
        return {
            'id': self.id,
            'transporte': self.transporte,
            'factor': self.factor
        }