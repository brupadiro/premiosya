from secciones.apuestas.models.apuesta1x2 import Apuesta1x2
from rest_framework import serializers
class apuesta1x2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Apuesta1x2
        fields = '__all__'


