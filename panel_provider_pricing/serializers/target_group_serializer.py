from rest_framework import serializers

from panel_provider_pricing.models import TargetGroup


class TargetGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetGroup
        fields = ["name", "external_id"]
