from django.db import models
from secciones.apuestas.models.apuesta import Apuesta


"""
Gracias a este tipo de apuesta, no perderá la apuesta si un partido termina en empate.
La casa de apuestas le devolverá el dinero en ese caso.
Esta apuesta resulta muy interesante si cree que uno de los equipos no tiene ninguna posibilidad de ganar,
pero puede lograr un empate.
"""
class ApuestaDevolucionEmpate(Apuesta):

    #Fields
    victoria_local = models.BooleanField()
    victoria_visitante = models.BooleanField()

    """
    def devolverApuesta():
        pass
    """
