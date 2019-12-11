from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.core import serializers
#models 
from secciones.apuestas.models.apuesta1x2 import Apuesta1x2
#from secciones.apuestas.models.apuesta import Apuesta
#serializers
from secciones.apuestas.serializers.apuesta1x2 import apuesta1x2Serializer
class apuesta1x2ViewSet(viewsets.ModelViewSet):
    """ViewSet for the Productos class"""

    queryset = Apuesta1x2.objects.all()
    serializer_class = apuesta1x2Serializer
    filter_backends = (SearchFilter,DjangoFilterBackend,OrderingFilter)
    #filter_fields = ("name", "country","owner__id","owner__studio","category__id","style__id")

    def create(self, request):
        data = request.data
        _apuestaSerializer = apuesta1x2Serializer(data = data)
        if _apuestaSerializer.is_valid(raise_exception = True):
            apuesta = _apuestaSerializer.save() 
            apuesta = apuestaSerializer(apuesta).data           
        return Response(apuesta, status.HTTP_201_CREATED)

    def update(self, request, pk = None):
        #creo la instancia
        instance = self.get_object()
        data = request.data
        _apuestaSerializer = apuesta1x2Serializer(instance, data = data)
        if _apuestaSerializer.is_valid(raise_exception = True):
            _apuestaSerializer.save()
            
        return Response(status.HTTP_201_CREATED)

