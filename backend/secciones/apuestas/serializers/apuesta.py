#Models
from secciones.apuestas.models.apuesta import Apuesta
from secciones.apuestas.models.juego import Juego
#Serializers
from secciones.apuestas.serializers.juego import JuegoSerializer
#DRF
from rest_framework import serializers

class apuestaSerializer(serializers.ModelSerializer):
    juego = JuegoSerializer(read_only=True)
    nombre_juego = serializers.CharField(max_length=35,write_only=True)
    class Meta:
        model = Apuesta
        fields = [
            'cantidad_apostada',
            'fecha',
            'juego',
            'resultado_descanzo',
            'resultado_final',
            'resultado_local',
            'resultado_visitante',
            'nombre_juego'
        ]
        #extra_kwargs = {'juego_name':{'write_only': True}}

    def create(self, validated_data):
        juego = Juego.objects.get(nombre_juego=validated_data['nombre_juego'])
        apuesta = Apuesta(
            cantidad_apostada = validated_data['cantidad_apostada'],
            fecha = validated_data['fecha'],
            juego = juego,
            resultado_descanzo = validated_data['resultado_descanzo'],
            resultado_final = validated_data['resultado_final'],
            resultado_local = validated_data['resultado_local'],
            resultado_visitante = validated_data['resultado_visitante']
        )
        apuesta.save()
        return apuesta



