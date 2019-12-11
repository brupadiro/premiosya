#Models
from secciones.apuestas.models.apuesta import Apuesta
from secciones.apuestas.models.juego import Juego
#Serializers
from secciones.apuestas.serializers.juego import JuegoSerializer
#DRF
from rest_framework import serializers

class apuestaSerializer(serializers.ModelSerializer):
    juego = JuegoSerializer(read_only=True)
    class Meta:
        model = Apuesta
        fields = [
            'resultado_1',
            'resultado_2',
            'created_at',
            'juego',
            'resultado_apuesta',
            'cantidad_apostada'
        ]
        #extra_kwargs = {'juego_name':{'write_only': True}}




