from django.db import models


class DeviceData(models.Model):
    dev_id = models.IntegerField(primary_key=True)
    lat = models.DecimalField(max_digits=15, decimal_places=8)
    lon = models.DecimalField(max_digits=15, decimal_places=8)

class TrafficData(models.Model):
    device = models.ForeignKey(DeviceData, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    macadd = models.CharField(max_length=12)
