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
    TokenAvailability,
)
from django.utils import timezone
from datetime import timedelta
from phonenumber_field.formfields import SplitPhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from phonenumber_field.formfields import PhoneNumberField
# service,Food,Accessories create,Update
class ServiceOfferedForm(forms.ModelForm):
    phone=PhoneNumberField(region="CA")

    


    class Meta:
        model = ServiceOffered
        fields = ["service_name", "price", "image"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class AccessoriesForm(forms.ModelForm):

    class Meta:
        model = Accessories
        fields = ["accessories_name", "price", "image", "total_stock"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class DogFoodForm(forms.ModelForm):

    class Meta:
        model = DogFood
        fields = ["Food_name", "price", "image", "total_stock"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


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
        self.fields["token"].required = True


class UpdateBookServiceOfferedForm(forms.ModelForm):

    class Meta:
        model = BookingService
        fields = ["token"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class BookAccessoriesForm(forms.ModelForm):
    accessories_name = forms.CharField(
        widget=forms.TextInput(attrs={"readonly": "readonly", "class": "form-control"})
    )

    class Meta:
        model = BookingAccessories
        fields = ["price", "quantity", "email", "address", "payement_mode"]

        widgets = {
            "price": forms.TextInput(
                attrs={"readonly": "readonly", "class": "form-control"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
            self.fields["quantity"].required = True
            self.fields["email"].required = True
            self.fields["address"].required = True
            self.fields["payement_mode"].required = True


class UpdateBookAccessoriesForm(forms.ModelForm):

    class Meta:
        model = BookingAccessories
        fields = ["email", "address"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class BookFoodForm(forms.ModelForm):
    Food_name = forms.CharField(
        widget=forms.TextInput(attrs={"readonly": "readonly", "class": "form-control"})
    )

    class Meta:
        model = BookingFood
        fields = ["price", "quantity", "email", "address", "payement_mode"]
        widgets = {
            "price": forms.TextInput(
                attrs={"readonly": "readonly", "class": "form-control"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

        self.fields["quantity"].required = True
        self.fields["email"].required = True
        self.fields["address"].required = True
        self.fields["payement_mode"].required = True


class UpdateBookFoodForm(forms.ModelForm):

    class Meta:
        model = BookingFood
        fields = ["email", "address"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


# checkup doctors
class DoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = "__all__"
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
        # token_visibility = Token.objects.filter(token_available=True)
        # token_date_visibility = TokenAvailability.objects.filter(is_available=True)
        # self.fields["Token"].queryset = token_visibility
        # self.fields["Token"].queryset = token_date_visibility
        # self.field["Token"].queryset = token_visibility

        doctors_available = Doctors.objects.filter(availability=True)
        self.fields["doctor_name"].queryset = doctors_available

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class AppointmentStatusForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ["status"]
        widgets = {"status": forms.Select(attrs={"class": "form-select"})}


class ServiceTokenForm(forms.ModelForm):
    class Meta:
        model = TokenService
        fields = ["token", "available"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class StatusUpdateAccessoriesForm(forms.ModelForm):
    class Meta:
        model = BookingAccessories
        fields = ["status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


class StatusUpdateFoodForm(forms.ModelForm):
    class Meta:
        model = BookingFood
        fields = ["status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
