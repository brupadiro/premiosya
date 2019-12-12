from django.urls import path, include
from rest_framework import routers

from secciones.apuestas.views.apuestas import apuestaViewSet
from secciones.apuestas.views.juegos import juegoViewSet

from secciones.apuestas.views.loteria.loterias import ResultadoLoteriaViewSet 
from secciones.apuestas.views.loteria.nueva_loteria import NuevaLoteriaViewSet   

router = routers.DefaultRouter()
router.register(r'apuestas', apuestaViewSet)
router.register(r'juegos',juegoViewSet)
router.register(r'loterias',ResultadoLoteriaViewSet)
router.register(r'nueva_loteria',NuevaLoteriaViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)
