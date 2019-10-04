from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from panel_provider_pricing.models.serializers import LocationSerializer
from panel_provider_pricing.queries import LocationsQuery
from panel_provider_pricing.services.validations.location import LocationParamsValidation
from panel_provider_pricing.views.api import BasePricingAPIView

@permission_classes([AllowAny])
class LocationsView(BasePricingAPIView, GenericAPIView):
    serializer_class = LocationSerializer

    def get(self, request, country_code):
        """
        Returns a JSON list of locations which belong to the selected country (based on its current panel provider)

        Params:
            country_code : str
        """

        params = self._location_params(country_code)
        params_validation = LocationParamsValidation(params)

        response = None

        if params_validation.passed():
            locations = LocationsQuery(params).call()
            response = self._serialized_ok_response(locations, many=True)
        else:
            response = self._bad_request_response(params_validation)

        return response


    def _location_params(self, country_code):
        return { "country_code": country_code }
