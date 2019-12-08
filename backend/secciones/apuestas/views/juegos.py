from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.core import serializers

#Models
from secciones.apuestas.models.juego import Juego
#Serializers
from secciones.apuestas.serializers.juego import JuegoSerializer

class juegoViewSet(viewsets.ModelViewSet):

    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend,OrderingFilter)
