from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)


class BasePricingAPIView(APIView):

    def _serialized_ok_response(self, queryset, many=False):
        serialized_data = self.get_serializer(queryset, many=many).data

        return Response(serialized_data, status=HTTP_200_OK)

    def _bad_request_response(self, failed_validation):
        return Response( { "error": failed_validation.errors_as_a_sentence() },
            status=HTTP_400_BAD_REQUEST)
