from django.db import models
from users.models import CustomUser


# Create your models here.
# class Shop(models.Model):
#     username = models.ForeignKey(CustomUser, on_delete=models.CASCADE,blank=True)
#     email = models.EmailField(blank=True)


class ServiceOffered(models.Model):
    service_name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="service_offered")
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.service_name


class Accessories(models.Model):
    total_stock = models.PositiveIntegerField(null=True, blank=True)

    accessories_name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="Accessories")
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self. accessories_name


class DogFood(models.Model):
    Food_name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="Food")
    price = models.PositiveIntegerField()


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
    
   


class BookingService(models.Model):
    service_name = models.ForeignKey(ServiceOffered, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()


class BookingAccessories(models.Model):
    total_stock = models.ForeignKey(
        Accessories, on_delete=models.CASCADE, related_name="stocks",null=True,blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)

    accessories_name = models.ForeignKey(Accessories, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    # def save(self, *args, **kwargs):
    #     if self.quantity > self.total_stock:
    #         raise ValueError("Quantity may be less than of Total Stock")
    #     if 
    #     return super().save()


class BookingFood(models.Model):
    Food_name = models.ForeignKey(DogFood, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()






##