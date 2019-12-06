from django.urls import path, include
from rest_framework import routers
from secciones.users.views.users import usersViewSet

router = routers.DefaultRouter()
router.register(r'users', usersViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)


