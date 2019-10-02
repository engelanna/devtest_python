from rest_framework import serializers

from panel_provider_pricing.models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["name"]
