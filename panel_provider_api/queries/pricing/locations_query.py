from django.shortcuts import get_object_or_404

from panel_provider_pricing.models import (
    Country,
    Location,
    LocationGroup
)


class LocationsQuery():

    def __init__(self, location_params):
        self.params = {
            "country_code": location_params["country_code"].upper(),
        }


    def call(self):

        country = get_object_or_404(Country,
            country_code=self.params["country_code"])
        location_group_ids = [lg.id for lg in LocationGroup.objects.filter(panel_provider_id=country.panel_provider_id)]

        return Location.objects.filter(location_groups__in=location_group_ids)
