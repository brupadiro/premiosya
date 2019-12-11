from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core import serializers
import requests
import xmltodict
import json

class matchesViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        channel = request.query_params.get("channel")
        page = 1 if request.query_params.get("page") else 1
        url = "http://feed.datafactory.la/?fechadesde=20191208&hora=100000&canal={}".format(channel)
        print(url)
        data = requests.get(url)
        xpars = xmltodict.parse(data.text,attr_prefix="", cdata_key="")
        fechas = xpars["fixture"]["fecha"]
        print(fechas)
        partidosADevolver = [] 
        for fecha in fechas:
            if fecha["estado"] == "actual":
                partidosADevolver = fecha

        return Response(partidosADevolver)

    @action(detail = False, methods = ['get'])
    def fichaMam(self,request,pk = None,channel=None,id=None):
        channel = request.query_params.get("channel")
        id = request.query_params.get("id")
        url = "http://feed.datafactory.la/?canal=deportes.futbol.{}.ficha.{}.htmlcenter".format(channel,id)
        print(url)
        data = requests.get(url)
        xpars = xmltodict.parse(data.text.replace("@",""),attr_prefix="", cdata_key="")
        return Response(xpars["ficha"]["fichapartido"])

    @action(detail = False, methods = ['get'])
    def feed(self,request,pk = None,channel=None,id=None):
        channel = request.query_params.get("channel")
        id = request.query_params.get("id")
        url = "http://feed.datafactory.la/?desde=20191207"
        print(url)
        data = requests.get(url)
        xpars = xmltodict.parse(data.text.replace("@",""),attr_prefix="", cdata_key="")
        return Response(xpars)

