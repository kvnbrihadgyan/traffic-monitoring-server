from rest_framework import routers, serializers
from .models import TrafficData, DeviceData

# Serializers define the API representation.
class TrafficDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrafficData

class DeviceDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceData
