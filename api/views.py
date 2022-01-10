from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import *
from api.serializers import *


# Create your views here.

@api_view(['GET', 'POST'])
def position_list(request):
    if request.method == 'GET':
        positions = Position.objects.all()
        serializer = PositionSerializer(positions, many=True)
        # return Response(status=status.HTTP_200_OK)
        return Response(serializer.data)
    elif request.method == 'POST':
        # serializer = PositionSerializer(data=request.data)
        # if serializer.is_valid():
        #     print(serializer.data)
        try:
            print(request.data)
            print(request.data['notify_data']['body']['services'][0])
            return Response(status=status.HTTP_200_OK)
        # except KeyError:
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def devices(request):
    if request.method == 'GET':
        try:
            user_id = request.GET.get('user_id')
            # devices = Device.objects.all()
            devices = Device.objects.filter(user_id=user_id)
            serializer = DeviceSerializer(devices, many=True)
            return Response(serializer.data)
        except Exception:
            return Response({"Error message": "Please query with user_id."},
                            status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            # Judging if the user have the device with the same name.
            print(serializer.validated_data)
            user_id = serializer.validated_data['user_id']
            name = serializer.validated_data['name']
            query = Device.objects.filter(user_id=user_id)
            for q in query:
                if q.name == name:
                    return Response({"Error message": "Name existed. Please rename your device."},
                                    status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






# @api_view(['POST'])
# def position_list(request):
#     if request.method == 'GET':
#         positions = Position.objects.all()
#         serializer = PositionSerializer(positions, many=True)
#         # return Response(status=HTTP_200_OK)
#         return Response(serializer.data)

