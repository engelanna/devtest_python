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


@permission_classes([AllowAny])
class LoginView(APIView):

    def post(self, request):
        """
        Private API login point

        JSON params: {
            "username": str,
            "password": str
        }

        Side effects:
            generates user token on successful authentication
        """

        username = request.data.get("username")
        password = request.data.get("password")

        if username is None or password is None:
          return Response({"error": "Please provide both username and password"}, status=HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user:
          token, _created = Token.objects.get_or_create(user=user)
          return Response({ "token": token.key }, status=HTTP_200_OK)
        else:
          return Response({ "error": "Invalid Credentials" }, status=HTTP_404_NOT_FOUND)
