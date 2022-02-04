from rest_framework import serializers
from django.contrib.auth.models import User


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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','email']
        extra_kwargs = {'password':{'write_only':True,'required':True}}
    def create(self,validated_data):
        if not validated_data.get('email'):
            raise ValueError('User must provide an email address to register')
        user = User.objects.create_user(**validated_data)
        return user