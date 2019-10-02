from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from panel_provider_pricing.models import Country, TargetGroup
from panel_provider_pricing.serializers import TargetGroupSerializer


@permission_classes([AllowAny])
class TargetGroupsView(APIView):

    def get(self, request, country_code):
        """
        Returns a JSON list of target groups which belong to the selected country (based on its current panel provider)

        Authentication:
            JSON web token

        Params:
            country_code : string
        """

        country = get_object_or_404(Country, country_code=country_code.upper())
        target_groups = TargetGroup.objects.filter(panel_provider_id=country.panel_provider_id)

        return Response(
            TargetGroupSerializer(target_groups, many=True).data
        )
