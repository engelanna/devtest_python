from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from panel_provider_pricing.models import Country


@permission_classes([IsAuthenticated])
class LocationsView(APIView):

    def get(self, request, country_code):
        """
        Returns a JSON list of locations which belong to the selected country (based on its current panel provider)

        Authentication:
            JSON web token

        Params:
            country_code : str
        """

        country = get_object_or_404(Country, country_code=country_code.upper())

        return redirect("api_v1_public_locations", country_code)
