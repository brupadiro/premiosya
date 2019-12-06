from django.db import models
from secciones.apuestas.models.apuesta import Apuesta

class ApuestaResultadoFinal(Apuesta):

    local = models.IntegerField(blank=False)
    visitante = models.IntegerField(blank=False)
