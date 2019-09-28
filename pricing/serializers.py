from rest_framework import serializers
from .models import Country, PanelProvider, Country, Location, LocationGroup, TargetGroup

class PanelProviderSerializer(serializers.Serializer):
  price = serializers.SerializerMethodField("price")
  #is_project = serializers.BooleanField(source='is_project')

  class Meta:
    model = PanelProvider
    fields = ("price")

  def price(self, obj):
    return {
      0: price_from_time_com_html_nodes,
      1: price_from_time_com_character_a_count,
      2: price_from_openlibrary_arrays
    }[obj.id % 3]()

  def price_from_time_com_html_nodes(self):
    pass

  def price_from_time_com_character_a_count(self):
    response = requests.get("https://time.com/")

    if response.status_code == requests.codes.ok:
      return response.text.count("a") / 100.0


  def price_from_openlibrary_arrays(self):
    pass

