from django.db import models
from secciones.apuestas.models.tipoApuesta import tipoApuesta
from secciones.users.models.users import Users
class Apuesta(models.Model):

    # Fields
    team_1 = models.CharField(max_length=200)
    team_2 = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    tipo_apuesta = models.ForeignKey(tipoApuesta,  on_delete=models.CASCADE)
    apuesta = models.IntegerField()