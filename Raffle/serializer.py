from rest_framework import serializers
from .models import Raffle

class RaffleSerializer(serializers.ModelSerializer):
    class Meta:
        #Referencia del modelo.
        model = Raffle
        fields = '__all__'