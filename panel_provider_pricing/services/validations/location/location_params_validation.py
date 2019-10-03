from panel_provider_pricing.services.validations import BaseValidation

class LocationParamsValidation(BaseValidation):

    def __init__(self, location_params):
        self.required_params = {
            "country_code": location_params["country_code"]
        }
