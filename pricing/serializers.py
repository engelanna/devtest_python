from collections.abc import Iterable
from rest_framework import serializers
from lxml import html
import requests

from .models import Country, PanelProvider, Country, Location, LocationGroup, TargetGroup

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["name"]

class TargetGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetGroup
        fields = ["name", "external_id"]

class PanelProviderSerializer(serializers.Serializer):
    price = serializers.SerializerMethodField("price")
    #is_project = serializers.BooleanField(source='is_project')

    def price(_self, obj):
        return {
          0: price_from_time_com_html_nodes,
          1: price_from_time_com_character_a_count,
          2: price_from_openlibrary_arrays
        }[obj.id % 3]()


    def price_from_time_com_html_nodes(self):
        response = requests.get("https://time.com/")

        if response.status_code == requests.codes.ok:
            html_node_count = html.fromstring(response.content).xpath(
                "count(//*)"
            )
            return html_node_count / 100.0

    def price_from_time_com_character_a_count(self):
        response = requests.get("https://time.com/")

        if response.status_code == requests.codes.ok:
          return response.text.count("a") / 100.0

    def price_from_openlibrary_arrays(self):
        response = requests.get("http://openlibrary.org/search.json?q=the+lord+of+the+rings")

        if response.status_code == requests.codes.ok:
            return __arrays_over_10_elements_count(response.json())


    def __arrays_over_10_elements_count(self, json, count=0):
        for value in __values_list(json):
            if __value_is_interesting(value):
                count += 1 if len(value) >= 10 else 0
                count = __arrays_over_10_elements_count(value, count)
        return count

    def __values_list(self, json):
        return json.values() if isinstance(json, dict) else json

    def __value_is_interesting(self, value):
        return isinstance(value, Iterable) and not isinstance(value, str)
