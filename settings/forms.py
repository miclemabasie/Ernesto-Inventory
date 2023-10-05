from .models import Settings
from django import forms


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ["company_name", "reorder_default", "logo", "timezone"]

        widgets = {
            "company_name": forms.TextInput(attrs={"class": "form-control"}),
            "reorder_default": forms.NumberInput(attrs={"class": "form-control"}),
            "timezone": forms.Select(attrs={"class": "form-control"}),
        }
