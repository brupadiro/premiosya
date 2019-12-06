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

    def create(self, request):
        data = request.data
        _apuestaSerializer = apuestaSerializer(data = data)
        if _apuestaSerializer.is_valid(raise_exception = True):
            apuesta = _apuestaSerializer.save() 
            apuesta = apuestaSerializer(apuesta).data           
        return Response(apuesta, status.HTTP_201_CREATED)

    def update(self, request, pk = None):
        #creo la instancia
        instance = self.get_object()
        data = request.data
        _apuestaSerializer = apuestaSerializer(instance, data = data)
        if _apuestaSerializer.is_valid(raise_exception = True):
            _apuestaSerializer.save()
            
        return Response(status.HTTP_201_CREATED)

