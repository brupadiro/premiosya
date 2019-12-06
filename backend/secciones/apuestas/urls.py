from django.urls import path, include
from rest_framework import routers

from secciones.apuestas.views.apuestas import apuestaViewSet
    

router = routers.DefaultRouter()
router.register(r'apuestas', apuestaViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)
