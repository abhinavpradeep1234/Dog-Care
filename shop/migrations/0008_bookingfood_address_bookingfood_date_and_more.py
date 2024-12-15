# Generated by Django 5.1.2 on 2024-12-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0007_bookingaccessories_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookingfood",
            name="address",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="bookingfood",
            name="date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="bookingfood",
            name="email",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="bookingfood",
            name="payement_mode",
            field=models.CharField(
                blank=True,
                choices=[("COD", "Cash on Delivery"), ("ONLINE", "Online Payment")],
                max_length=200,
                null=True,
            ),
        ),
    ]
