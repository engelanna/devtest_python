from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND
)

from panel_provider_pricing.services.validations.user import UserParamsValidation, UserAuthentication
from panel_provider_pricing.views.api import BasePricingAPIView


@permission_classes([AllowAny])
class LoginView(BasePricingAPIView):
    """
    Private API login point

    JSON params: {
        "username": str,
        "password": str
    }

    Side effects:
        on successful authentication, generates user token
    """

    def post(self, request):
        response = None
        user_params = self._user_params(request)
        params_validation = UserParamsValidation(user_params)

        if params_validation.passed():
            response = self._authentication_response(user_params)
        else:
            response = self._bad_request_response(params_validation)

        return response


    def _user_params(self, request):
        return {
            "username": request.data.get("username"),
            "password": request.data.get("password"),
        }


    def _authentication_response(self, params):
        response = None
        user_authentication = UserAuthentication(params)

        if user_authentication.passed():
            token, _created = Token.objects.get_or_create(
                user=user_authentication.user)
            response = self._authentication_successful_response(token)
        else:
          response = self._authentication_failed_response()

        return response

    def _authentication_successful_response(self, token):
        return Response({ "token": token.key },
            status=HTTP_200_OK)

    def _authentication_failed_response(self):
        return Response({ "error": "Invalid Credentials" },
            status= HTTP_404_NOT_FOUND)

