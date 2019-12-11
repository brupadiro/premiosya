from django.db import models
class categoriasPartidos(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
