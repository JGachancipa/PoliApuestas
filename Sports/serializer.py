from rest_framework import serializers

from Sports.models import Championship

# Serializador de Campeonatos
class ChampionshipSerializer (serializers.ModelSerializer):
    class Meta:
        model = Championship
        fields = '__all__'