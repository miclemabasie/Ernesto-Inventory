from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(verbose_name=_("Category"), max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def get_number_products(self) -> int:
        return len(Category.objects.filter(name=self.name))

    def get_products(self) -> list:
        queryset = Category.objects.filter(name=self.name)
        return queryset

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    user = models.ForeignKey(
        User, related_name="products", on_delete=models.SET_NULL, null=True
    )
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(verbose_name=_("Product Name"), max_length=250)
    price = models.FloatField(
        verbose_name=_("Product's Price"),
        help_text="In XAF",
        default=0.00,
        null=True,
        blank=True,
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Products's Quantity"), default=0
    )
    image = models.ImageField(verbose_name=_("Image"), upload_to="products")
    reorder_level = models.PositiveIntegerField(verbose_name=_("Reorder Level"))
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "products"
