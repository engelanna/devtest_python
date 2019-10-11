from panel_provider_pricing.services.validations import BaseValidation


class TargetGroupParamsValidation(BaseValidation):

    def __init__(self, target_group_params):
        self.required_params = {
            "country_code": target_group_params["country_code"]
        }
