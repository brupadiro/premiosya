from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.core import serializers
#models 
from secciones.apuestas.models.loteria.resultado_loteria import ResultadoLoteria
#serializers
from secciones.apuestas.serializers.loteria.resultado_loteria_serializer import ResultadoLoteriaSerializer

class ResultadoLoteriaViewSet(viewsets.ModelViewSet):

    queryset = ResultadoLoteria.objects.all()
    serializer_class = ResultadoLoteriaSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend,OrderingFilter)
    filter_fields = ('loteria_id',)
    