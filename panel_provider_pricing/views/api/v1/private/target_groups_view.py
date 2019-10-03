from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from panel_provider_pricing.models import Country


@permission_classes([IsAuthenticated])
class TargetGroupsView(APIView):

    def get(self, request, country_code):
        """
        Returns a JSON list of target groups which belong to the selected country (based on its current panel provider)

        Authentication:
            JSON web token

        Params:
            country_code : string
        """

        return redirect("api_v1_public_target_groups", country_code)
