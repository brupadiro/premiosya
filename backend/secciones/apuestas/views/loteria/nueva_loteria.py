from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.core import serializers
# Models
from secciones.apuestas.models.loteria.loteria import Loteria   
# Serializers
from secciones.apuestas.serializers.loteria.loteria_serializer import LoteriaSerializer

class NuevaLoteriaViewSet(viewsets.ModelViewSet):

    queryset = Loteria.objects.all()
    serializer_class = LoteriaSerializer