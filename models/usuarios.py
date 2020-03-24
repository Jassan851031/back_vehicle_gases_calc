import sqlite3
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    __table_args__ = { 'extend_existing': True }

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
        }
