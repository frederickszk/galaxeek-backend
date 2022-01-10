from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import *
from api.serializers import *


# Create your views here.

@api_view(['GET'])
def position_list(request):
    if request.method == 'GET':
        positions = Position.objects.all()
        serializer = PositionSerializer(positions, many=True)
        return Response(serializer.data)

