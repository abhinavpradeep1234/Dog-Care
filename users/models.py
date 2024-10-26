from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


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
