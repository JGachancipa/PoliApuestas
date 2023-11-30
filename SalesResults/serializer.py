from rest_framework import serializers

from SalesResults.models import SalesResults

class SalesResultsSerializer (serializers.ModelSerializer):
    class Meta:
        model = SalesResults
        fields = '__all__'