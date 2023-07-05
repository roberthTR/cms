from rest_framework import serializers
from . import models

# Crear clase serializador
class ClienteSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = models.Cliente
        fields = '__all__'

class TipoContenidoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = models.TipoContenido
        fields = '__all__'

class SistemaCMSSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = models.SistemaCMS
        fields = '__all__'

