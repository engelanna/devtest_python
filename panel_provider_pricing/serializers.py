from collections.abc import Iterable
from rest_framework import serializers
from lxml import html
import requests

from .models import Country, PanelProvider, Country, Location, LocationGroup, TargetGroup


class PanelProviderSerializer(serializers.Serializer):
    class Meta:
        model = PanelProvider
        fields = ["price"]

    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        return {
          0: self._price_from_time_com_html_nodes,
          1: self._price_from_time_com_character_a_count,
          2: self._price_from_openlibrary_arrays
        }[obj.id % 3]()

    def _price_from_time_com_html_nodes(self):
        response = requests.get("https://time.com/")

        if response.status_code == requests.codes.ok:
            html_node_count = html.fromstring(response.content).xpath(
                "count(//*)"
            )
            return html_node_count / 100.0

    def _price_from_time_com_character_a_count(self):
        response = requests.get("https://time.com/")

        if response.status_code == requests.codes.ok:
          return response.text.count("a") / 100.0

    def _price_from_openlibrary_arrays(self):
        response = requests.get("http://openlibrary.org/search.json?q=the+lord+of+the+rings")

        if response.status_code == requests.codes.ok:
            return self._arrays_over_10_elements_count(response.json())


    def _arrays_over_10_elements_count(self, json, count=0):
        for value in self._values_list(json):
            if self._value_is_interesting(value):
                count += 1 if len(value) >= 10 else 0
                count = self._arrays_over_10_elements_count(value, count)
        return count

    def _values_list(self, json):
        return json.values() if isinstance(json, dict) else json

    def _value_is_interesting(self, value):
        return isinstance(value, Iterable) and not isinstance(value, str)
