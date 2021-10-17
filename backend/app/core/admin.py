from django.contrib import admin
from core.models import Sample, Device, DeviceConfig, SensorReading



admin.site.register(Sample)


@admin.register(SensorReading)
class SensorReadingAdmin(admin.ModelAdmin):
    model = SensorReading

@admin.register(Device)
class TagAdmin(admin.ModelAdmin):
    model = Device

@admin.register(DeviceConfig)
class TagAdmin(admin.ModelAdmin):
    model = DeviceConfig

