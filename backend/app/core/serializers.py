from rest_framework import serializers

from .models import DeviceConfig, SensorReading, Sample

class DeviceConfigSerializer(serializers.HyperlinkedModelSerializer):
    #device = serializers.UUIDField(source='device.id')
    class Meta:
        model = DeviceConfig
        fields = ('bpm', 'duty','ledState','pressureMax')

class SensorReadingSerializer(serializers.HyperlinkedModelSerializer):
    device = serializers.UUIDField(source='device.id')
    class Meta:
        model = SensorReading
        fields = ('time','device','ledState', 'solenoidState','pumpState','psi')

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ['attachment']