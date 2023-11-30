from rest_framework import serializers

from AdwardsPublicationsBet.models import AdwardsPublicationsBet

class AdwardsPublicationsBetSerializer (serializers.ModelSerializer):
    class Meta:
        model = AdwardsPublicationsBet
        fields = '__all__'