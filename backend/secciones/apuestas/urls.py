from django.urls import path, include
from rest_framework import routers

from secciones.apuestas.views.apuestas import apuestaViewSet
from secciones.apuestas.views.juegos import juegoViewSet
    

router = routers.DefaultRouter()
router.register(r'apuestas', apuestaViewSet)
router.register(r'juegos',juegoViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)
