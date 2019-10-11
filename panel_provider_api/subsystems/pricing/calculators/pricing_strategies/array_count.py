from collections.abc import Iterable
from lxml import html
import requests

from panel_provider_pricing.services.crawlers import FetchJSONResponse


class ArrayCount():
    """
    Counts arrays longer than <min_array_length> in the input
    """

    def __init__(self,
                 min_array_length = 10,
                 target_url="http://openlibrary.org/search.json?q=the+lord+of+the+rings",
                 divisor=100.0):
        self.min_array_length = min_array_length
        self.target_url = target_url
        self.divisor = divisor


    def execute(self):
        crawler = FetchJSONResponse(self.target_url)
        response = crawler.execute()

        if crawler.last_response_ok:
            return self._arrays_over_10_elements_count(response)


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
