from rest_framework import serializers

from Sports.models import Championship

class ChampionshipSerializer (serializers.ModelSerializer):
    class Meta:
        model = Championship
        fields = '__all__'