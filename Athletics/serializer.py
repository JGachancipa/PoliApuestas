from rest_framework import serializers

from Athletics.models import Athletics

# Serializador de Campeonatos
class AthleticsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Athletics
        fields = '__all__'