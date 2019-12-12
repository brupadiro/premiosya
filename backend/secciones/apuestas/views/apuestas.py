from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.core import serializers
#models 
from secciones.apuestas.models.apuesta import Apuesta
#serializers
from secciones.apuestas.serializers.apuesta import apuestaSerializer
class apuestaViewSet(viewsets.ModelViewSet):
    """ViewSet for the Productos class"""

    queryset = Apuesta.objects.all()
    serializer_class = apuestaSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend,OrderingFilter)
    filter_fields = ('juego__nombre_juego',)

