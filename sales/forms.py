from django import forms
from .models import SaleItem


class SaleItemForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = ("product", "quantity", "unit_price", "total_price", "created")

        widgets = {
            "product": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "unit_price": forms.NumberInput(attrs={"class": "form-control"}),
            "total_price": forms.NumberInput(attrs={"class": "form-control"}),
            "created": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
