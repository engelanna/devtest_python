from panel_provider_pricing.services.validations import BaseValidation


class UserParamsValidation(BaseValidation):

    def __init__(self, user_params):
        self.username = user_params["username"]
        self.password = user_params["password"]


    def passed(self):
        if self.username is None or self.password is None:
            return False
        else:
            return True

