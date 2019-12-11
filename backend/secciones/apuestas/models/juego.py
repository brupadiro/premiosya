from django.db import models

class Juego(models.Model):

    valor_ficha = models.PositiveIntegerField()
    nombre_juego = models.CharField(max_length=35,blank=False, null=False)

    def __str__(self):
        return self.nombre_juego
