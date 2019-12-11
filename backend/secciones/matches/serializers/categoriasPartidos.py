#Models
from secciones.matches.models.categoriasPartidos import categoriasPartidos
#DRF
from rest_framework import serializers

class categoriasPartidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoriasPartidos
        fields = [
            'nombre',
            'codigo'
        ]




