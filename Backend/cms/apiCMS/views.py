from django.shortcuts import render
from rest_framework import viewsets
from . import models,serializers

# Create your views here.

class cliente(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializers_class= serializers.ClienteSerializer

class tipoContenido(viewsets.ModelViewSet):
    queryset = models.TipoContenido.objects.all()
    serializers_class= serializers.TipoContenidoSerializer

class sistemaCMS(viewsets.ModelViewSet):
    queryset = models.SistemaCMS.objects.all()
    serializers_class= serializers.SistemaCMSSerializer
