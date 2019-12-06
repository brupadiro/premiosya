from django.db import models
from secciones.apuestas.models.apuesta import Apuesta

"""
Apuesta a dos de los tres resultados posibles.
Si cree que es imposible que pierda el equipo local, apueste a 1X (victoria en casa o empate).
Esta apuesta aumenta sus posibilidades de beneficio, pero en detrimento de la cuota.

"""

class ApuestaDoble(Apuesta):

    victoriaLocal_empate = models.BooleanField()
