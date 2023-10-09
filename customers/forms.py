from django import forms
from .models import Customer


class CustomerAddForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "phone", "email", "address"]

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name of Customer"}
            ),
            "phone": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Phone Number"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Customer's E-mail"}
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Customer's Address"}
            ),
        }


class SendMailForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter you message"}
        )
    )
