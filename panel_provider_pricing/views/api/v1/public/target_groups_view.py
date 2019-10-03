from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from panel_provider_pricing.models.serializers import TargetGroupSerializer
from panel_provider_pricing.queries import TargetGroupsQuery
from panel_provider_pricing.services.validations import TargetGroupParamsValidation


@permission_classes([AllowAny])
class TargetGroupsView(APIView):
    serializer_class = TargetGroupSerializer

    def get(self, request, country_code):
        """
        Returns a JSON list of target groups which belong to the selected country (based on its current panel provider)

        Authentication:
            JSON web token

        Params:
            country_code : string
        """

        params = self._target_group_params(country_code)
        params_validation = TargetGroupParamsValidation.new(params)

        response = None

        if params_validation.passed():
            target_groups = TargetGroupsQuery(params).call();
            response = self._serialize_ok_response(target_groups)
        else:
            response = self._bad_request_response(params_validation)

        return response


    def _target_group_params(self, country_code):
        return { "country_code": country_code }

    def _serialize_ok_reponse(self, target_groups):
        return Response(
            get_serializer(target_groups, many=True).data,
            status=HTTP_200_OK)

    def _bad_request_response(self, failed_validation):
        return Response({ "error": failed_validation.errors_as_a_sentence() },
            status=HTTP_400_BAD_REQUEST)
