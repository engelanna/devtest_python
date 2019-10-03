from django.contrib.auth import authenticate

from panel_provider_pricing.services.validations import BaseValidation


class UserAuthentication(BaseValidation):

    def __init__(self, user_params):
        username = user_params["username"]
        password = user_params["password"]
        self.user = authenticate(username=username, password=password)


    def passed(self):
        if self.user:
            return True
        else:
            return False
