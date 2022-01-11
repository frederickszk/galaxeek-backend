from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Device(models.Model):
    user_id = models.BigIntegerField()
    device_id_iot = models.CharField(max_length=100)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)


class Position(models.Model):
    device_id = models.BigIntegerField()
    # device = models.ForeignKey(Device, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)


