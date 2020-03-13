from rest_framework import serializers

from api.models import Data


class DataSerializer(serializers.ModelSerializer):
    cpi_val = serializers.FloatField(read_only=True)

    date = serializers.DateField(required=False)
    country = serializers.CharField(max_length=255, required=False)
    channel = serializers.CharField(max_length=255, required=False)
    os = serializers.CharField(max_length=255, required=False)
    impressions = serializers.IntegerField(required=False)
    clicks = serializers.FloatField(required=False)
    installs = serializers.FloatField(required=False)
    spend = serializers.FloatField(required=False)
    revenue = serializers.FloatField(required=False)

    class Meta:
        model = Data
        fields = '__all__'
