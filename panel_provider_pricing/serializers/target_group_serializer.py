from rest_framework import serializers


class TargetGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetGroup
        fields = ["name", "external_id"]
