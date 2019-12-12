from django.db import models
from secciones.users.models.users import Users

class Loteria(models.Model):

    usuario = models.ForeignKey(Users,on_delete=models.CASCADE)
    activa = models.BooleanField()

    def __str__(self):
        return "Apuesta numero:{} de {}".format(self.pk,self.usuario)
    