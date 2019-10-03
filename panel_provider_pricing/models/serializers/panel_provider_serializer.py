from rest_framework import serializers

from panel_provider_pricing.models import PanelProvider


class PanelProviderSerializer(serializers.Serializer):
    price = serializers.SerializerMethodField()


    class Meta:
        model = PanelProvider
        fields = ["price"]


    def get_price(self, panel_provider):
        return globals()[panel_provider.price_calculation_strategy]
