from rest_framework import serializers

from .models import DeviceConfig, SensorReading

class DeviceConfigSerializer(serializers.HyperlinkedModelSerializer):
    device = serializers.UUIDField(source='device.id')
    class Meta:
        model = DeviceConfig
        fields = ('id','device','bpm', 'duty','ledState','pressureMax')

class SensorReadingSerializer(serializers.HyperlinkedModelSerializer):
    device = serializers.UUIDField(source='device.id')
    class Meta:
        model = SensorReading
        fields = ('time','device','ledState', 'solenoidState','pumpState','psi')