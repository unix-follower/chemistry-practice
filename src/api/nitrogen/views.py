from rest_framework.response import Response
from rest_framework.views import APIView

from src.api.common.serializers import ElementCalcResultResponseSerializer
from src.component import nitrogen_facade
from src.component import constants


class NitrogenView(APIView):
    def get(self, request):
        molecules = float(request.query_params[constants.MOLECULES])
        result = nitrogen_facade.calculate_mass(molecules)
        response_serializer = ElementCalcResultResponseSerializer(instance=result)
        return Response(response_serializer.data)
