# Generated by Django 5.1.4 on 2025-01-06 06:08

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_alter_bookingaccessories_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="serviceoffered",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, region=None
            ),
        ),
    ]
