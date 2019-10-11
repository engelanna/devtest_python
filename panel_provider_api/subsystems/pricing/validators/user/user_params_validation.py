from panel_provider_pricing.services.validations import BaseValidation


class UserParamsValidation(BaseValidation):

    def __init__(self, user_params):
        self.required_params = {
            "username": user_params["username"],
            "password": user_params["password"]
        }


    def errors_as_a_sentence(self):
        "Please provide both username and password"
