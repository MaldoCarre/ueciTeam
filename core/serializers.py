from rest_framework import serializers
from.models import Departamentos,Tipo_ciberdelito,Tipo_incidente,Plataforma,Denuncia

class DenunciaSerializada (serializers.ModelSerializer):
    class Meta:
        model = Denuncia
        fields = '__all__'

class DepartamentosSerializada (serializers.ModelSerializer):
    class Meta:
        model = Departamentos
        fields = '__all__'
class TipociberdelitoSerializada (serializers.ModelSerializer):
    class Meta:
        model = Tipo_ciberdelito
        fields = '__all__'

class TipoincidenteSerializada (serializers.ModelSerializer):
    class Meta:
        model = Tipo_incidente
        fields = '__all__'
class PataformaSerializada (serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = '__all__'