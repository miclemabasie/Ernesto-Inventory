from django import forms
from .models import SaleItem
from products.models import Product
from django.shortcuts import get_object_or_404


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

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        quantity = cleaned_data.get("quantity")
        product = cleaned_data.get("product")
        # get product:
        if quantity > product.quantity:
            raise forms.ValidationError(
                "Quantity can not be greater than available product quantity!"
            )
        return cleaned_data
