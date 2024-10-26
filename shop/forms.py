from django import forms
from shop.models import BookingService, BookingAccessories, BookingFood
from shop.models import (
    ServiceOffered,
    Accessories,
    DogFood,
    Doctors,
    Token,
    Appointment,
)
from django.utils import timezone
from datetime import timedelta

class BookServiceOfferedForm(forms.ModelForm):
    class Meta:
        model = BookingService
        fields = ["service_name", "price"]


class BookAccessoriesForm(forms.ModelForm):
    class Meta:
        model = BookingAccessories
        fields = ["accessories_name", "price", "quantity"]
        
    
    # def __init__(self, *args, **kwargs):
    #     super(Accessories, self).__init__(*args, **kwargs)
    #     self.fields['accessories_name'].widget.attrs['readonly'] = True
    #     self.fields['price'].widget.attrs['readonly'] = True



class BookFoodForm(forms.ModelForm):
    class Meta:
        model = BookingFood
        fields = ["Food_name", "price"]

    # def __init__(self,*args, **kwargs):
    # super().__init__(self,*args, **kwargs)
    # self.field.['price'].pref


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
    # def __init__(self, *args, **kwargs):
    #     super(Accessories, self).__init__(*args, **kwargs)
    #     self.fields['accessories_name'].widget.attrs['readonly'] = True
    #     self.fields['price'].widget.attrs['readonly'] = True



class DogFoodForm(forms.ModelForm):

    class Meta:
        model = DogFood
        fields = ["Food_name", "price", "image"]
        widgets = {
            "Food_name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }


class DoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ["doctor_name", "specialized"]
        widgets = {
            "doctor_name": forms.TextInput(attrs={"class": "form-control"}),
            "specialized": forms.TextInput(attrs={"class": "form-control"}),
        }


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
        widgets = {"appointment_date":forms.DateInput(attrs={"class":"form-control","type":"date"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        available = Token.objects.filter(token_available=True)
        self.fields["Token"].queryset = available
        
        today=timezone.localtime().date()
        self.fields["appointment_date"].widget.attrs['min']=today.strftime('%Y-%m-%d')
        
        max_date = (today + timedelta(days=2)).strftime('%Y-%m-%d')

        self.fields["appointment_date"].widget.attrs['max']=max_date

        





