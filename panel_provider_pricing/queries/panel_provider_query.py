from django.shortcuts import get_object_or_404

from panel_provider_priving.models import Country

class PanelProviderQuery():

    def __init__(self, panel_params):
        self.params = {
            "country_code": panel_params["country_code"],
            "target_group_id": panel_params["target_group_id"],
            "locations": panel_params["locations"]
        }


    def call(self):
        panel_provider = get_object_or_404(Country,
            country_code=self.params["country_code"]
        ).select_related("panel_provider")

        return panel_provider

