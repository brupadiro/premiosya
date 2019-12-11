import unittest
from django.urls import reverse
from django.test import Client
from .models import Productos
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_usuarios(**kwargs):
    defaults = {}
    defaults["rut"] = "rut"
    defaults["descripcion"] = "descripcion"
    defaults["precio"] = "precio"
    defaults["descuento"] = "descuento"
    defaults["nombre"] = "nombre"
    defaults["categoria"] = "categoria"
    defaults["activa"] = "activa"
    defaults["imagen_principal"] = "imagen_principal"
    defaults.update(**kwargs)
    return Productos.objects.create(**defaults)


class usuariosViewTest(unittest.TestCase):
    '''
    Tests for Productos
    '''
    def setUp(self):
        self.client = Client()

    def test_list_usuarios(self):
        url = reverse('producto_usuarios_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_usuarios(self):
        url = reverse('producto_usuarios_create')
        data = {
            "rut": "rut",
            "descripcion": "descripcion",
            "precio": "precio",
            "descuento": "descuento",
            "nombre": "nombre",
            "categoria": "categoria",
            "activa": "activa",
            "imagen_principal": "imagen_principal",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_usuarios(self):
        Productos = create_usuarios()
        url = reverse('producto_usuarios_detail', args=[Productos.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_usuarios(self):
        Productos = create_usuarios()
        data = {
            "rut": "rut",
            "descripcion": "descripcion",
            "precio": "precio",
            "descuento": "descuento",
            "nombre": "nombre",
            "categoria": "categoria",
            "activa": "activa",
            "imagen_principal": "imagen_principal",
        }
        url = reverse('producto_usuarios_update', args=[Productos.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


