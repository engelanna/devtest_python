from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny

from panel_provider_pricing.models.serializers import TargetGroupSerializer
from panel_provider_pricing.queries import TargetGroupsQuery
from panel_provider_pricing.services.validations.target_group import TargetGroupParamsValidation
from panel_provider_pricing.views.api import BasePricingAPIView

@permission_classes([AllowAny])
class TargetGroupsView(BasePricingAPIView, GenericAPIView):
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
        params_validation = TargetGroupParamsValidation(params)

        response = None

        if params_validation.passed():
            target_groups = TargetGroupsQuery(params).call();
            response = self._serialized_ok_response(target_groups, many=True)
        else:
            response = self._bad_request_response(params_validation)

        return response


    def _target_group_params(self, country_code):
        return { "country_code": country_code }
