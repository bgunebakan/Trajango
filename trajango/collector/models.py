from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=200)
    dev_id = models.IntegerField()


class Location(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    altitude = models.FloatField(default=0)

    hdop = models.FloatField(default=0)
    speed = models.FloatField(default=0)

    timestamp = models.DateTimeField()
