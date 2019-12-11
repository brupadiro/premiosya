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
    #filter_fields = ("name", "country","owner__id","owner__studio","category__id","style__id")



    @action(detail=False)
    def apuesta2X1(self,request):

        nombre_juego = "2X1"
        apuestas2X1 = Apuesta.objects.filter(juego__nombre_juego=nombre_juego)
        serializer = self.get_serializer(apuestas2X1,many=True)
        return Response(serializer.data)
