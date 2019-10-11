from django.contrib.auth import authenticate

from panel_provider_pricing.services.validations import BaseValidation


class UserAuthentication(BaseValidation):

    def __init__(self, user_params):
         self.username = user_params["username"]
         self.password = user_params["password"]


    def passed(self):
        self.user = authenticate(
            username=self.username, password=self.password
        )

        return True if self.user else False
