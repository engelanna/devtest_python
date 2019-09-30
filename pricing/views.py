from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.views import APIView
import json

from .models import Country, Location, LocationGroup, TargetGroup
from .serializers import *


@permission_classes([AllowAny])
class LoginView(APIView):
    """
    Private API entry point
    """
    def post(self, request):
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


@permission_classes([AllowAny])
class PublicLocationsView(APIView):
    """
    Returns locations which belong to the selected country based on its current panel provider
    """
    def get(self, request, country_code):
        country = get_object_or_404(Country, country_code=country_code.upper())
        location_group_ids = [lg.id for lg in LocationGroup.objects.filter(panel_provider_id=country.panel_provider_id)]
        locations = Location.objects.filter(location_groups__in=location_group_ids)

        return Response(LocationSerializer(locations, many=True).data)


@permission_classes([AllowAny])
class PublicTargetGroupsView(APIView):
    """
    Returns target groups which belong to the selected country based on it's current panel provider
    """
    def get(self, request, country_code):
        country = get_object_or_404(Country, country_code=country_code.upper())
        target_groups = TargetGroup.objects.filter(panel_provider_id=country.panel_provider_id)

        return Response(
            TargetGroupSerializer(target_groups, many=True).data
        )


@permission_classes([IsAuthenticated])
class PrivateLocationsView(APIView):

    def get(self, request, country_code):
        country = get_object_or_404(Country, country_code=country_code.upper())

        return redirect("locations", country_code)


@permission_classes([IsAuthenticated])
class PrivateTargetGroupsView(APIView):

    def get(self, request, country_code):
        country = get_object_or_404(Country, country_code=country_code.upper())

        return redirect("target_groups", country_code)


@permission_classes([IsAuthenticated])
class PrivatePricingView(APIView):
    """
    Returns a price based on the panel provider used by a country

    provided and valid:

    :country_code
    :target_group_id
    :locations (an array of hashes which look like this { id: 123, panel_size: 200 })
    """
    def post(self, request):
        self.__check_required_params(request)

        country = get_object_or_404(
            Country, country_code=request.POST["country_code"].upper()
        )
        target_group = get_object_or_404(
            TargetGroup, id=request.POST["target_group_id"]
        )
        locations = self.__get_locations(request)

        return Response(
            PanelProviderSerializer(country.panel_provider).data
        )

    def __check_required_params(self, request):
        for field in ["country_code", "target_group_id", "locations"]:
                if not field in request.POST:
                    raise KeyError("Required field missing: %s" % field)

    def __get_locations(self, request):
        locations = []

        for location in json.loads(request.POST["locations"]):
            if not isinstance(location, dict):
                raise ValueError(
                    "Not a hash: %s, %s" % (type(location), location)
                )

            locations.append(
                get_object_or_404(Location,
                    id=location["id"],
                    panel_size=location["panel_size"]))

        return locations
