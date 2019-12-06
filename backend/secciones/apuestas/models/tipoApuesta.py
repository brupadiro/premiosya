from django.db import models

class tipoApuesta(models.Model):

    # Fields
    name = models.CharField(max_length=200,)
    pagoPorFicha = models.IntegerField()
