# Models
from secciones.apuestas.models.loteria.loteria import Loteria
# DRF
from rest_framework import serializers

class LoteriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Loteria
        fields  = '__all__'