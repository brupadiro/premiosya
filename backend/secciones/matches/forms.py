from django import forms
from .models import Productos


class usuariosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['rut', 'descripcion', 'precio', 'descuento', 'nombre', 'categoria', 'activa', 'imagen_principal']


