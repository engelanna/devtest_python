from django.shortcuts import get_object_or_404#, render
from django.http import HttpResponse
from .models import Country
from .serializers import PanelProviderSerializer
# PanelProvider, Country, Location, LocationGroup, TargetGroup
from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

@permission_classes([AllowAny])
class PrivateAPILogin(APIView):

  def post(_, request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
      return Response({"error": "Please provide both username and password"}, status=HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if user:
      token, _ = Token.objects.get_or_create(user=user)
      return Response({"token": token.key}, status=HTTP_200_OK)
    else:
      return  Response({"error": "Invalid Credentials"}, status=HTTP_404_NOT_FOUND)



"""
Z tym bawieniem sie (droga do flow) zamiast walki:

Należy wypróbować wariację do pomidorów: "przez najbliższe 25 minut będę się tylko bawić, dopiero potem zacznę pracować".
2 MIN AGO
"""



class PanelProviderViewSet(RetrieveModelMixin, GenericViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = Country.objects.all()
    lookup_field = "country_code"
    serializer_class = PanelProviderSerializer

def request_1(request, country_code):
  """Returns locations which belong to the selected country based on its current panel provider"""
  country = get_object_or_404(Country, country_code=country_code)
  location_group_ids = [lg.id for lg in LocationGroup.objects.filter(panel_provider_id=country.panel_provider_id)]
  return Location.objects.filter(location_groups__in=location_group_ids)


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
