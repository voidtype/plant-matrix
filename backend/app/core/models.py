from django.db import models
from django.conf import settings
import uuid
import traceback
import psycopg2.errors
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

#note when a user is created, so we can generate a token for them
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Device(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    long = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

class Sample(models.Model):
    attachment = models.FileField()
    device = models.ForeignKey(Device,on_delete=models.CASCADE)

class SensorReading(models.Model):
    time = models.DateTimeField(primary_key=True, default=datetime.now)
    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    psi = models.FloatField()
    ledState = models.IntegerField()
    solenoidState = models.IntegerField()
    pumpState = models.IntegerField()
    
    #let's overload the save function to account for pk collisions on the time var
    def save(self, *args, **kwargs):
        traceback.print_stack()
        self.save_and_smear_timestamp(*args, **kwargs)
    
    def save_and_smear_timestamp(self, *args, **kwargs):
        """Recursivly try to save by incrementing the timestamp on duplicate error"""
        try:
            super().save(*args, **kwargs)
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
    device = models.OneToOneField(Device,primary_key=True,on_delete=models.CASCADE)
    bpm = models.DecimalField(max_digits=22, decimal_places=3, blank=True, null=True, default=0.5)
    duty = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True, default=0.022)
    ledState = models.IntegerField(
        default=255,
        validators=[MaxValueValidator(255), MinValueValidator(0)]
     )
    pressureMax = models.IntegerField( blank=True, null=True, default=70, validators=[MaxValueValidator(255), MinValueValidator(10)])
