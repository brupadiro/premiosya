from django.db import models
from secciones.apuestas.models.apuesta import Apuesta

"""
Este tipo de apuesta combina el resultado en el descanso y el resultado al final de los 90 minutos.
Para ganar la apuesta hay que pronosticar el resultado en el descanso
y el resultado al final del tiempo reglamentario.
"""

class ApuestaDescanzoFinal(Apuesta):

    res_descanzo = models.IntegerField(blank=False)
    res_final = models.IntegerField(blank=False)