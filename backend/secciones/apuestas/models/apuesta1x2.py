from django.db import models

from secciones.users.models.users import Users
from secciones.apuestas.models.apuesta import Apuesta


"""
Es la apuesta más fácil de entender, pero también la más difícil de jugar.
El 1 indica la victoria del equipo local,
la X un empate y el 2 significa la victoria del equipo visitante.
"""
class Apuesta1x2(Apuesta):

    #Fields
    victoria_local = models.BooleanField()
    empate = models.BooleanField()
    victoria_visitante = models.BooleanField()
