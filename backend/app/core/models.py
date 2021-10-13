from django.db import models
from django.conf import settings
import uuid
import traceback
import psycopg2.errors
from datetime import datetime

class Sample(models.Model):
    attachment = models.FileField()

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.get_username()

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

class Device(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    long = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

class SensorReading(models.Model):
    time = models.DateTimeField(primary_key=True, default=datetime.now)
    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    psi = models.FloatField()
    ledState = models.BooleanField()
    solenoidState = models.BooleanField()
    pumpState = models.BooleanField()
    
    #let's overload the save function to account for pk collisions on the time var
    def save(self, *args, **kwargs):
        traceback.print_stack()
        self.save_and_smear_timestamp(*args, **kwargs)
    
    def save_and_smear_timestamp(self, *args, **kwargs):
        """Recursivly try to save by incrementing the timestamp on duplicate error"""
        try:
            super().save(*args, **kwargs)
            print("saved via super")
        except psycopg2.errors.UniqueViolation as exception:
            print("oh no")
            # Only handle the error:
            #   psycopg2.errors.UniqueViolation: duplicate key value violates unique constraint "1_1_farms_sensorreading_pkey"
            #   DETAIL:  Key ("time")=(2020-10-01 22:33:52.507782+00) already exists.
            if all (k in exception.args[0] for k in ("Key","time", "already exists")):
                # Increment the timestamp by 1 µs and try again
                self.time = str(datetime.fromisoformat(self.time) + datetime.timedelta(microseconds=1))
                self.save_and_smear_timestamp(*args, **kwargs)

class DeviceConfig(models.Model):
    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    bpm = models.DecimalField(max_digits=22, decimal_places=5, blank=True, null=True, default=0.5)
    duty = models.DecimalField(max_digits=22, decimal_places=5, blank=True, null=True, default=0.022)
    ledState = models.BooleanField(default=False)
    pressureMax = models.DecimalField(max_digits=22, decimal_places=5, blank=True, null=True, default=70)
