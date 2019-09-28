from rest_framework import serializers
from .models import Country, PanelProvider, Country, Location, LocationGroup, TargetGroup

class PanelProviderSerializer(serializers.Serializer):
  class Meta:
    model = PanelProvider
    fields = ("price")

  def price(self, obj):
    obj.price()
