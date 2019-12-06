from django.db import models
from secciones.apuestas.models.tipoApuesta import tipoApuesta
from secciones.users.models.users import Users
class Pocisiones(models.Model):

    # Fields
    jugador = models.ForeignKey(Users, on_delete=models.CASCADE)
    deporte = models.CharField(max_length=50)
    puntaje = models.IntegerField()
