from django.urls import path, include
from rest_framework import routers

from secciones.matches.views.matches import matchesViewSet
    

router = routers.DefaultRouter()
router.register(r'matches', matchesViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)
