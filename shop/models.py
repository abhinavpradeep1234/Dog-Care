from django.db import models
from users.models import CustomUser
from django.core.exceptions import ValidationError


# Doggy Essentials
class ServiceOffered(models.Model):
    service_name = models.CharField(max_length=300)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="service_offered_image")

    def __str__(self):
        return self.service_name


class Accessories(models.Model):
    total_stock = models.PositiveIntegerField(null=False, blank=False, default=1)

    accessories_name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="Accessories")
    price = models.PositiveIntegerField()
    username = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.accessories_name


class DogFood(models.Model):
    total_stock = models.PositiveIntegerField(null=True, blank=True, default=0)

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
    date = models.DateTimeField(auto_now=True, editable=False)

    


class BookingAccessories(models.Model):
    PAYEMENT = (
        ("COD", "Cash on Delivery"),
        ("ONLINE", "Online Payment"),
    )

    total_stock = models.ForeignKey(
        Accessories,
        on_delete=models.CASCADE,
        related_name="stocks",
        null=True,
        blank=True,
    )
    username = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, blank=True
    )
    quantity = models.PositiveIntegerField(
        null=False, blank=False, default=1
    )  # This makes the field required

    accessories_name = models.ForeignKey(
        Accessories, on_delete=models.CASCADE, null=True, blank=True
    )
    price = models.PositiveIntegerField(null=True, blank=True)
    total_price = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now=True, editable=False)
    payement_mode = models.CharField(
        max_length=200, choices=PAYEMENT, null=True, blank=True,help_text="NB : If you choose online payment, after completing the payment you need to click  confirm button otherwise order will not be placed"
    )

    def save(self, *args, **kwargs):
        self.total_price = self.price * self.quantity
        if self.quantity < 1:
            raise ValidationError("Quantity must be at least 1")
        if self.total_stock:
            # if self.total_stock.total_stock == 0:
            #     raise ValidationError("OUT OF STOCK")
            if self.total_stock.total_stock < self.quantity:
                raise ValidationError(
                    "Quantity must be less than or equal to available stock"
                )

        return super().save(*args, **kwargs)


class BookingFood(models.Model):
    PAYEMENT = (
        ("COD", "Cash on Delivery"),
        ("ONLINE", "Online Payment"),
    )

    Food_name = models.ForeignKey(DogFood, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(null=False, blank=False, default=1)
    total_stock = models.ForeignKey(
        DogFood, on_delete=models.CASCADE, related_name="stocks", null=True, blank=True
    )
    username = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True
    )
    total_price = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now=True, editable=False)
    payement_mode = models.CharField(
        max_length=200, choices=PAYEMENT, null=True, blank=True ,help_text="NB : If you choose online payment, after completing the payment you need to click  'confirm booking' button to confirm order otherwise order will not be placed"
    )

    def save(self, *args, **kwargs):
        self.total_price = self.price * self.quantity
        if self.quantity < 1:
            raise ValidationError("quantity must be At least 1")
        if self.total_stock:

            if self.total_stock.total_stock < self.quantity:
                raise ValidationError(
                    "Quantity must be less than or equal to available stock"
                )

        return super().save(*args, **kwargs)


# Checkup Details DOctors Token And booking Appointment
class Doctors(models.Model):
    doctor_name = models.CharField(max_length=200, unique=True, blank=True)
    specialized = models.CharField(max_length=200, blank=True)
    availability=models.BooleanField(default=True)

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
    is_available = models.BooleanField(
        default=True
    )  # Specific availability for this date

    class Meta:
        unique_together = ("token", "date")  # Ensure each token-date pair is unique

    def __str__(self):
        return f"{self.token} - {self.date} - {'Available' if self.is_available else 'Unavailable'}"


class Appointment(models.Model):
    # AVAILABE FIELD added for status
    STATUS = (
        ("confirm booking", "Confirm Booking"),
        (
            "finished",
            "Finished",
        ),
        ("pending", "Pending"),
    )
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    doctor_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    Token = models.ForeignKey(Token, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=STATUS, default="pending")
    appointment_date = models.DateField()
