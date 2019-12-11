from django.urls import path, include
from rest_framework import routers

from secciones.matches.views.matches import matchesViewSet
from secciones.matches.views.categoriasPartidos import categoriasPartidosViewset
    

router = routers.DefaultRouter()
router.register(r'matches', matchesViewSet,basename='matches')
router.register(r'categoriaspartidos', categoriasPartidosViewset,basename='categoriaspartidos') 

urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)
