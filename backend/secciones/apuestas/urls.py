from django.urls import path, include
from rest_framework import routers

from secciones.apuestas.views.apuesta1x2 import apuesta1x2ViewSet
#from secciones.apuestas.views.apuestas import apuestaViewSet
    

router = routers.DefaultRouter()
router.register(r'apuesta1x2', apuesta1x2ViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)
