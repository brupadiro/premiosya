from django.db import models
from secciones.apuestas.models.loteria.loteria import Loteria

class ResultadoLoteria(models.Model):

    estado_opciones = [

        ('PERDIO','PERDIO'),
        ('GANO','GANO'),
        ('PENDIENTE','PENDIENTE'),
    ]

    resultado_total = models.PositiveIntegerField(blank=False,null=False)
    loteria = models.ForeignKey(Loteria,on_delete=models.CASCADE)
    id_partido = models.PositiveIntegerField()
    estado_resultado = models.CharField(max_length=9,choices=estado_opciones)

