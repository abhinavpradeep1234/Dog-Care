# Generated by Django 5.1.2 on 2024-12-23 08:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("shop", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="accessories",
            name="username",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="appointment",
            name="username",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="bookingaccessories",
            name="accessories_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.accessories",
            ),
        ),
        migrations.AddField(
            model_name="bookingaccessories",
            name="total_stock",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="stocks",
                to="shop.accessories",
            ),
        ),
        migrations.AddField(
            model_name="bookingaccessories",
            name="username",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="bookingfood",
            name="username",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="bookingservice",
            name="username",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="appointment",
            name="doctor_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="shop.doctors"
            ),
        ),
        migrations.AddField(
            model_name="bookingfood",
            name="Food_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="shop.dogfood"
            ),
        ),
        migrations.AddField(
            model_name="bookingfood",
            name="total_stock",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="stocks",
                to="shop.dogfood",
            ),
        ),
        migrations.AddField(
            model_name="bookingservice",
            name="service_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="shop.serviceoffered"
            ),
        ),
        migrations.AddField(
            model_name="appointment",
            name="Token",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="shop.token"
            ),
        ),
        migrations.AddField(
            model_name="tokenavailability",
            name="token",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="shop.token"
            ),
        ),
        migrations.AddField(
            model_name="bookingservice",
            name="token",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.tokenservice",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="tokenavailability",
            unique_together={("token", "date")},
        ),
    ]
