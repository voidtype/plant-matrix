from rest_framework import serializers

from .models import DeviceConfig

class DeviceConfigSerializer(serializers.HyperlinkedModelSerializer):
    device = serializers.UUIDField(source='device.id')
    class Meta:
        model = DeviceConfig
        fields = ('id','device','bpm', 'duty','ledState','pressureMax')