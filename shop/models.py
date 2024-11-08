from django.db import models
from users.models import CustomUser


# Doggy Essentials
class ServiceOffered(models.Model):
    service_name = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to="service_offered", null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.service_name


class Accessories(models.Model):
    total_stock = models.PositiveIntegerField(null=True, blank=True)

    accessories_name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="Accessories")
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.accessories_name


class DogFood(models.Model):
    total_stock = models.PositiveIntegerField(null=True, blank=True)

    Food_name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="Food")
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.Food_name


# token Service
class TokenService(models.Model):
    token = models.CharField(max_length=200, null=True, blank=True, unique=True)

    available = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.token


# Booking Doggy Essentials
class BookingService(models.Model):
    service_name = models.ForeignKey(ServiceOffered, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    username = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, blank=True
    )
    token = models.ForeignKey(
        TokenService, on_delete=models.CASCADE, null=True, blank=True
    )
    

class BookingAccessories(models.Model):
    total_stock = models.ForeignKey(
        Accessories,
        on_delete=models.CASCADE,
        related_name="stocks",
        null=True,
        blank=True,
    )
    quantity = models.PositiveIntegerField(null=True, blank=True)

    accessories_name = models.ForeignKey(Accessories, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    total_price=models.PositiveIntegerField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.total_price=self.price*self.quantity
        return super().save(*args, **kwargs)
    


class BookingFood(models.Model):
    Food_name = models.ForeignKey(DogFood, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(null=True, blank=True)
    
    # def save(self, *args, **kwargs):
    #     self.total_price=self.price*self.quantity
    #     return super().save(*args, **kwargs)


# Checkup Details DOctors Token And booking Appointment
class Doctors(models.Model):
    doctor_name = models.CharField(max_length=200, unique=True, blank=True)
    specialized = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.doctor_name


class Token(models.Model):
    Token = models.CharField(max_length=200, unique=True)

    token_available = models.BooleanField(default=True)

    def __str__(self):
        return self.Token


class TokenAvailability(models.Model):
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    date = models.DateField()
    is_available = models.BooleanField(default=True)  # Specific availability for this date

    class Meta:
        unique_together = ('token', 'date')  # Ensure each token-date pair is unique

    def __str__(self):
        return f"{self.token} - {self.date} - {'Available' if self.is_available else 'Unavailable'}"


class Appointment(models.Model):
    STATUS = (
        ("CONFIRM BOOKING", "CONFIRM BOOKING"),
        (
            "FINISHED",
            "FINISHED",
        ),
    )
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    doctor_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    Token = models.ForeignKey(Token, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=STATUS, default="CONFIRM BOOKING")
    appointment_date = models.DateField()
