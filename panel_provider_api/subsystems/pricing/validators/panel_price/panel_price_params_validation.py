import json

from panel_provider_pricing.services.validations import BaseValidation


class PanelPriceParamsValidation(BaseValidation):

    def __init__(self, panel_price_params):
        super().__init__()

        self.required_params = {
            "country_code": panel_price_params["country_code"],
            "target_group_id": panel_price_params["target_group_id"],
            "locations": panel_price_params["locations"]
        }


    def passed(self):
        return super().passed() and self._locations_are_valid()


    def _locations_are_valid(self):
        passed = True

        for location in json.loads(self.required_params["locations"]):
            if not isinstance(location, dict):
                passed = False
                self.error_messages.append(
                    f"Not a JSON hash: {type(location)}, {location}"
                )

        return passed
