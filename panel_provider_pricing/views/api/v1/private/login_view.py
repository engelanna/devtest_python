from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.views import APIView

from panel_provider_pricing.services.validations import UserParamsValidation, UserAuthentication


@permission_classes([AllowAny])
class LoginView(APIView):
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
        user_params = self._user_params(request)
        response = None

        if UserParamsValidation(user_params).passed():
            response = _authentication_response(user_params)
        else:
            response = _missing_params_response()

        return response


    def _user_params(self, request):
        return {
            "username": request.data.get("username"),
            "password": request.data.get("password"),
        }

    def _authentication_response(self, params):
        user_authentication = UserAuthentication(params)
        response = None

        if user_authentication.passed():
            token, _created = Token.objects.get_or_create(
                user=user_authentication.user)
            response = Response({ "token": token.key }, status=HTTP_200_OK)
        else:
          response = Response({ "error": "Invalid Credentials" }, status=  HTTP_404_NOT_FOUND)

        return response

    def _missing_params_response(self):
        return Response({"error": "Please provide both username and password"}, status=HTTP_400_BAD_REQUEST)
