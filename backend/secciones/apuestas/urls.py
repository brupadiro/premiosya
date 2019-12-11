from django.urls import path, include
from rest_framework import routers

<<<<<<< HEAD
from secciones.apuestas.views.apuesta1x2 import apuesta1x2ViewSet
#from secciones.apuestas.views.apuestas import apuestaViewSet
    

router = routers.DefaultRouter()
router.register(r'apuesta1x2', apuesta1x2ViewSet)
=======
from secciones.apuestas.views.apuestas import apuestaViewSet
from secciones.apuestas.views.juegos import juegoViewSet
    

router = routers.DefaultRouter()
router.register(r'apuestas', apuestaViewSet)
router.register(r'juegos',juegoViewSet)
>>>>>>> e9b1c37fadf927fbac581f73a6bad7fe045bbbdf

urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)
