from secciones.apuestas.models.apuesta import Apuesta
from rest_framework import serializers
class apuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apuesta
        fields = (
            'team_1', 
            'team_2', 
            'date', 
            'user',
            'tipo_apuesta',
            'apuesta'
        )


