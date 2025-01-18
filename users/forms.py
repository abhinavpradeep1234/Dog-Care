from django import forms
from .models import CustomUser, Offers, Complaints
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].help_text = ""
        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={"class": "form-control"}
        )


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=200,
    )
    password = forms.CharField(
        max_length=15,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password"].widget = forms.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["username"].widget = forms.TextInput(
            attrs={"class": "form-control"}
        )


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "role"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "role": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].help_text = " "

        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={"class": "form-control"}
        )


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offers
        fields = ["offers"]
        widgets = {"offers": forms.TextInput(attrs={"class": "form-control"})}


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ["report","email"]
        widgets = {"report": forms.TextInput(attrs={"class": "form-control"})}


class ComplaintRespondForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ["responds"]
        widgets = {"responds": forms.TextInput(attrs={"class": "form-control"})}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

        self.fields["username"].help_text = " "
