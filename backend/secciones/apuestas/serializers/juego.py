from rest_framework import serializers
from secciones.apuestas.models.juego import Juego

class JuegoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Juego
        exclude = ['id']