from mongoengine import Document, StringField, FloatField, DateTimeField, BooleanField

class Transaccion(Document):
    tipo = StringField(choices=['compra', 'redención'], required=True)
    monto = FloatField(required=True)
    tarjeta_id = StringField(required=True)  # ID de la tarjeta
    fecha = DateTimeField()
    estado = StringField(choices=['completada', 'fallida'], default='completada')
    descripcion = StringField()  # Descripción opcional
