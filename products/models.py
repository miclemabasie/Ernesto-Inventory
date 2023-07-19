from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(verbose_name=_("Category"), max_length=250)
    slug = models.SlugField(verbose_name=_("Category Slug"), null=True, blank=True)

    def get_number_products(self) -> int:
        return len(Category.objects.filter(name=self.name))

    def get_products_count(self) -> list:
        cat = Category.objects.get(name__iexact=self.name)
        queryset = Product.objects.filter(category=cat)
        return queryset.count()

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Categories"


class Product(TimeStampedModel):
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
    slug = models.SlugField(verbose_name=_("Product Slug"), null=True, blank=True)
    quantity = models.PositiveIntegerField(
        verbose_name=_("Products's Quantity"), default=0
    )
    image = models.ImageField(
        verbose_name=_("Image"), upload_to="products", null=True, blank=True
    )
    reorder_level = models.PositiveIntegerField(verbose_name=_("Reorder Level"))
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "products"
