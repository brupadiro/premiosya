# Model
from secciones.apuestas.models.loteria.resultado_loteria import ResultadoLoteria
from secciones.apuestas.serializers.loteria.loteria_serializer import LoteriaSerializer
# DRF
from rest_framework import serializers

class ResultadoLoteriaSerializer(serializers.ModelSerializer):
    
    data_loteria = LoteriaSerializer(source="loteria",read_only = True)

    class Meta:
        
        model = ResultadoLoteria
        fields = [
            'resultado_total',
            'id_partido',
            'estado_resultado',
            'loteria',
            'data_loteria'
            ]
        #extra_kwargs = {'data_loteria':{'read_only':True}}

