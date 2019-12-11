from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core import serializers
import requests
import xmltodict
import json
from secciones.matches.models.categoriasPartidos import categoriasPartidos
from secciones.matches.serializers.categoriasPartidos import categoriasPartidosSerializer

class categoriasPartidosViewset(viewsets.ModelViewSet):

    queryset = categoriasPartidos.objects.all()
    serializer_class = categoriasPartidosSerializer