from rest_framework import serializers

from Prize.models import Prize

class PrizeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = '__all__'