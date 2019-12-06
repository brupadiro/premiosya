from rest_framework import viewsets, permissions, status
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
        channel = request.data["channel"]
        url = "http://feed.datafactory.la/?canal={}".format(channel)
        data = requests.get(url)
        xpars = xmltodict.parse(data.text)
        response = json.dumps(xpars)
        return Response(response)


