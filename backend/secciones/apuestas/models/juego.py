from django.db import models

class Juego(models.Model):

    valor_ficha = models.PositiveIntegerField()
    nombre_juego = models.CharField(blank=False, null=False)
