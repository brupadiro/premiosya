from django.db import models
from secciones.apuestas.models.tipoApuesta import tipoApuesta
from secciones.users.models.users import Users

class Apuesta(models.Model):

    user = models.ForeignKey(Users,on_delete=True)
    #partido = models.ForeignKey(Partido,on_delete=False)

    class Meta:
        abstract = True