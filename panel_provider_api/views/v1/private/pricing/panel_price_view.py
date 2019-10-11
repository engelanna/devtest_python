from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from panel_provider_pricing.models import Country
from panel_provider_pricing.models.serializers import PanelProviderSerializer
from panel_provider_pricing.queries import PanelProviderQuery
from panel_provider_pricing.services.validations.panel_price import PanelPriceParamsValidation
from panel_provider_pricing.views.api import BasePricingAPIView


@permission_classes([IsAuthenticated])
class PanelPriceView(BasePricingAPIView, GenericAPIView):
    serializer_class = PanelProviderSerializer

    def post(self, request):
        """
        What's the cost of launching a panel study, with x participants, in location y?

        Returns:
            price: a price based on the panel provider used by a country, considering the number of study participants

        Params:
            country_code : string
            target_group_id : integer
            locations : array of hashes like { "id": 123, "panel_size": 200 }

        Side effect:
            HTTP connections to external sites
        """

        params = self._panel_price_params(request)
        params_validation = PanelPriceParamsValidation(params)

        response = None

        if params_validation.passed():
            panel_provider = PanelProviderQuery(params).call();
            response = self._serialized_ok_response(panel_provider)
        else:
            response = self._bad_request_response(params_validation)

        return response


    def _panel_price_params(self, request):
        post_data = request.POST

        return {
            "country_code": post_data["country_code"].upper(),
            "target_group_id": post_data["target_group_id"],
            "locations": post_data["locations"]
        }


