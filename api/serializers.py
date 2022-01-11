from rest_framework import serializers
from .models import User, Device, Position


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'password']


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'user_id', 'device_id_iot', 'name', 'type']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'device_id', 'longitude', 'latitude', 'time']

