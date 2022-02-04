# Generated by Django 3.2.8 on 2021-10-12 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_device_deviceconfig_sensorreading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceconfig',
            name='bpm',
            field=models.DecimalField(blank=True, decimal_places=5, default=0.5, max_digits=22, null=True),
        ),
        migrations.AlterField(
            model_name='deviceconfig',
            name='duty',
            field=models.DecimalField(blank=True, decimal_places=5, default=0.022, max_digits=22, null=True),
        ),
        migrations.AlterField(
            model_name='deviceconfig',
            name='pressureMax',
            field=models.DecimalField(blank=True, decimal_places=5, default=70, max_digits=22, null=True),
        ),
    ]