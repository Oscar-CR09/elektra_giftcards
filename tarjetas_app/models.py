from django.db import models
from mongoengine import Document, StringField, FloatField, DateTimeField, ListField, EmailField, BooleanField

class Tarjeta(Document):
    tipo = StringField(choices=['física', 'digital'], required=True)
    monto = FloatField(required=True)
    fecha_vencimiento = DateTimeField()
    producto_especifico = StringField()  # Para tarjetas de productos específicos
    correo_asociado = EmailField()  # Solo para tarjetas digitales
    tipo_uso = StringField(choices=['único', 'múltiple'], required=True)
    estado = StringField(choices=['activa', 'usada', 'vencida'], default='activa')
    saldo = FloatField(default=0)  # Para tarjetas de uso múltiple
    fecha_emision = DateTimeField()
