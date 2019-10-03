import json

from panel_provider_pricing.services.validations import BaseValidation


class PanelPriceParamsValidation(BaseValidation):

    def __init__(self, panel_price_params):
        self.params = {
            "country_code": panel_price_params["country_code"],
            "target_group_id": panel_price_params["target_group_id"],
            "locations": panel_price_params["locations"]
        }
        self.error_messages = []


    def passed(self):
        return self._all_params_present() and self._locations_are_valid()


    def errors_as_a_sentence(self):
        return ". ".join(self.error_messages)


    def _all_params_present(self):
        passsed = True

        for param in self.params.keys():
            if not param:
                passed = False
                self.error_messages.append(
                    f"Missing parameter: {param}"
                )

        return passed

    def _locations_are_valid(self):
        passed = True

        for location in json.loads(self.params["locations"]):
            if not isinstance(location, dict):
                passed = False
                self.error_messages.append(
                    f"Not a hash: {type(location)}, {location}"
                )
