from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from panel_provider_pricing.models import Country
from panel_provider_pricing.models.serializers import PanelProviderSerializer
from panel_provider_pricing.queries import PanelProviderQuery
from panel_provider_pricing.services.validations import PanelPriceParamsValidation


@permission_classes([IsAuthenticated])
class PanelPriceView(APIView):
    queryset = PanelProviderQuery(self._panel_params).call()
    serializer_class = PanelProviderSerializer

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

        response = None
        params_validation = PanelPriceParamsValidation.new(
            self._panel_params(request))

        if params_validation.passed():
            panel_provider = self.get_queryset();
            response = self._serialized_ok_response(panel_provider)
        else:
            response = self._bad_request_response(params_validation)

        return response


    def _panel_params(self, request):
        post_data = request.POST

        return {
            country_code: post_data["country_code"].upper(),
            target_group_id: post_data["target_group_id"],
            locations: post_data["locations"]
        }

    def _bad_request_response(self, params_validation):
        return Response( { "error": params_validation.errors_as_a_sentence() },
            status=HTTP_400_BAD_REQUEST)

    def _serialized_ok_response(self, panel_provider):
        serialized_data = self.get_serializer(panel_provider).data

        return Response(serialized_data, status=HTTP_200_OK)
