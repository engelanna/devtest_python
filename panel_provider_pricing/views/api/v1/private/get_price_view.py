from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from panel_provider_pricing.models import Country
from panel_provider_pricing.serializers import PanelProviderSerializer


@permission_classes([IsAuthenticated])
class GetPriceView(APIView):

    def post(self, request):
        """
        What's the cost of launching a panel study, with x participants, in location y?

        Returns:
            price: a price based on the panel provider used by a country, considering the number of study participants

        Params:
            country_code : string
            target_group_id : integer
            locations :  an array of hashes like { id: 123, panel_size: 200 }

        Side effect:
            HTTP connections to external sites
        """

        self._check_required_params(request)

        country = get_object_or_404(
            Country, country_code=request.POST["country_code"].upper()
        )
        target_group = get_object_or_404(
            TargetGroup, id=request.POST["target_group_id"]
        )
        locations = self._get_locations(request)

        return Response(
            PanelProviderSerializer(country.panel_provider).data
        )

    def _check_required_params(self, request):
        for field in ["country_code", "target_group_id", "locations"]:
            if not field in request.POST:
                raise KeyError(F"Required field missing: {field}")

    def _get_locations(self, request):
        locations = []

        for location in json.loads(request.POST["locations"]):
            if not isinstance(location, dict):
                raise ValueError(
                    F"Not a hash: {type(location)}, {location}"
                )

            locations.append(
                get_object_or_404(Location,
                    id=location["id"],
                    panel_size=location["panel_size"]))

        return locations
