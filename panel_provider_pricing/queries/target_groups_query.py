from panel_provider_pricing.models import Country, TargetGroup

class TargetGroupsQuery():
    def __init__(self, panel_params):
        self.params = {
            "country_code": panel_params["country_code"].upper(),
        }


    def call(self):
        country = get_object_or_404(Country,
            country_code=self.params["country_code"])

        return TargetGroup.objects.filter(panel_provider_id=country.panel_provider_id)


