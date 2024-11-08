from mongoengine import Document, StringField, EmailField, ListField

class Usuario(Document):
    correo = EmailField(required=True)
    tarjetas_asociadas = ListField(StringField())  # IDs de tarjetas digitales
