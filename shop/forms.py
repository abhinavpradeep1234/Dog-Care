from django import forms
from shop.models import BookingService, BookingAccessories, BookingFood
from shop.models import (
    ServiceOffered,
    Accessories,
    DogFood,
    Doctors,
    Token,
    Appointment,
    TokenService,
)
from django.utils import timezone
from datetime import timedelta


# service,Food,Accessories create,Update
class ServiceOfferedForm(forms.ModelForm):

    class Meta:
        model = ServiceOffered
        fields = ["service_name", "price", "image"]
        widgets = {
            "service_name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }


class AccessoriesForm(forms.ModelForm):

    class Meta:
        model = Accessories
        fields = ["accessories_name", "price", "image", "total_stock"]
        widgets = {
            "accessories_name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }


class DogFoodForm(forms.ModelForm):

    class Meta:
        model = DogFood
        fields = ["Food_name", "price", "image", "total_stock"]
        widgets = {
            "Food_name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }


# booking service,Food,Accessories create,Update
class BookServiceOfferedForm(forms.ModelForm):
    service_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"})
    )

    class Meta:
        model = BookingService
        fields = ["price", "token"]
        widgets = {
            "price": forms.TextInput(
                attrs={"readonly": "readonly", "class": "form-control"}
            ),
            "token": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Limit available tokens
        self.fields["token"].queryset = TokenService.objects.filter(available=True)


class BookAccessoriesForm(forms.ModelForm):
    accessories_name = forms.CharField(
        widget=forms.TextInput(attrs={"readonly": "readonly", "class": "form-control"})
    )

    class Meta:
        model = BookingAccessories
        fields = [ "price", "quantity"]

        widgets = {
            "accessories_name": forms.TextInput(
                attrs={"class": "form-control", "readonly": "readonly"}
            ),
            "price": forms.NumberInput(
                attrs={"readonly": "readonly", "class": "form-control"}
            ),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
        }


class BookFoodForm(forms.ModelForm):
    Food_name = forms.CharField(
        widget=forms.TextInput(attrs={"readonly": "readonly", "class": "form-control"})
    )

    class Meta:
        model = BookingFood
        fields = ["price", "quantity"]
        widgets = {
            "Food_name": forms.Select(
                attrs={"class": "form-select"}
            ),
            "price": forms.TextInput(
                attrs={ "class": "form-control","readonly": "readonly"}
            ),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
        }


# checkup doctors
class DoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ["doctor_name", "specialized"]
        widgets = {
            "doctor_name": forms.TextInput(attrs={"class": "form-control"}),
            "specialized": forms.TextInput(attrs={"class": "form-control"}),
        }


# checkup Token


class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ["Token", "token_available"]
        widgets = {
            "Token": forms.TextInput(attrs={"class": "form-control"}),
            "token_available": forms.CheckboxInput(attrs={"class": "form-c"}),
        }


class BookingAppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = [
            "doctor_name",
            "appointment_date",
            "Token",
        ]
        widgets = {
            "appointment_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        available = Token.objects.filter(token_available=True)
        self.fields["Token"].queryset = available

        today = timezone.localtime().date()
        self.fields["appointment_date"].widget.attrs["min"] = today.strftime("%Y-%m-%d")

        max_date = (today + timedelta(days=2)).strftime("%Y-%m-%d")

        self.fields["appointment_date"].widget.attrs["max"] = max_date






class AppointmentStatusForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ["status"]
        widgets = {
            "status": forms.Select(
                attrs={"class": "form-select"}
            )
        }

class ServiceTokenForm(forms.ModelForm):
    class Meta:
        model = TokenService
        fields = ["token", "available"]
