# Generated by Django 5.1.2 on 2024-11-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('confirm booking', 'Confirm Booking'), ('finished', 'Finished'), ('rescheduled', 'Rescheduled')], default='CONFIRM BOOKING', max_length=200),
        ),
    ]
