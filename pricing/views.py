from django.shortcuts import get_object_or_404#, render
from django.http import HttpResponse
from .models import Country
from .serializers import PanelProviderSerializer
# PanelProvider, Country, Location, LocationGroup, TargetGroup
from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin


from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
  username = request.data.get("username")
  password = request.data.get("password")

  if username is None or password is None:
    return Response({"error": "Please provide both username and password"}, status=HTTP_400_BAD_REQUEST)

  user = authenticate(username=username, password=password)

  if not user:
    return Response({"error": "Invalid Credentials"}, status=HTTP_404_NOT_FOUND)

  token, _ = Token.objects.get_or_create(user=user)

  return Response({"token": token.key}, status=HTTP_200_OK)


class PanelProviderViewSet(RetrieveModelMixin, GenericViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = Country.objects.all()
    lookup_field = "country_code"
    serializer_class = PanelProviderSerializer

def request_1(request, country_code):
  country = get_object_or_404(Country, country_code=country_code) #  get_list_or_404()

  return HttpResponse("Hi there! You are at %s" % country.country_code)

def request_2(request, country_code):
  return HttpResponse("Hi there! You are at request_2.")

# POST evaluate_target
def request_3(request):
  country = get_object_or_404(Country, country_code=request.POST["country_code"])

  return HttpResponseRedirect(reverse("request_2", args=(country.country_code,)))

def request_4(request, country_code):
  return HttpResponse("Hi there! You are at request_4.")

def request_5(request, country_code):
  return HttpResponse("Hi there! You are at request_5.")
