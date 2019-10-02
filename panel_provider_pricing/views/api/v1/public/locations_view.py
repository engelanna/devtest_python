from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from panel_provider_pricing.models import Country, Location, LocationGroup
from panel_provider_pricing.serializers import LocationSerializer

@permission_classes([AllowAny])
class LocationsView(APIView):

    def get(self, request, country_code):
        """
        Returns a JSON list of locations which belong to the selected country (based on its current panel provider)

        Params:
            country_code : str
        """

        country = get_object_or_404(Country, country_code=country_code.upper())
        location_group_ids = [lg.id for lg in LocationGroup.objects.filter(panel_provider_id=country.panel_provider_id)]
        locations = Location.objects.filter(location_groups__in=location_group_ids)

        return Response(LocationSerializer(locations, many=True).data)
