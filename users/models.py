from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# from shop.models import Accessories, ServiceOffered, DogFood


class CustomUser(AbstractUser):
    ROLE = (("SHOP OWNER", "SHOP OWNER"),)
    role = models.CharField(max_length=200, choices=ROLE, blank=True)


class Notification(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    notification = models.CharField(max_length=250)
    is_read = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)


class Offers(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    offers = models.CharField(max_length=250)
    time = models.DateTimeField(auto_now=True)


class Complaints(models.Model):
    username = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, blank=True
    )
    reported_date = models.DateTimeField(auto_now=True, editable=False)
    report = models.CharField(max_length=300, null=True, blank=True)
    responds = models.CharField(max_length=300, null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
