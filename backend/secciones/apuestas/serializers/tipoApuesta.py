from secciones.apuestas.models.tipoApuesta import tipoApuesta
from rest_framework import serializers

class tipoApuestaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = tipoApuesta
        fields = (
            'name',
            'pagoPorFicha' 
        )
