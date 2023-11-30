from rest_framework import serializers

from AdwardsPublications.models import AdwardsPublications

class AdwardsPublicationsSerializer (serializers.ModelSerializer):
    class Meta:
        model = AdwardsPublications
        fields = '__all__'