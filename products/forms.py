from django import forms
from .models import Product, Category


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "category",
            "price",
            "quantity",
            "reorder_level",
            "active",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "reorder_level": forms.NumberInput(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def on_create(self):
        name = self.cleaned_data.get("name")
        # Check if product in database already with same name
        try:
            product = Product.objects.get(name__iexact=name)
            if product:
                raise forms.ValidationError("Product with same name alread exists!")
        except Product.DoesNotExist:
            return name


class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        # Check if product in database already with same name
        try:
            category = Category.objects.get(name__iexact=name)
            if category:
                raise forms.ValidationError("Category with same name alread exists!")
        except Product.DoesNotExist:
            return name
