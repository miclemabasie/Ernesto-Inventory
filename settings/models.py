from django.shortcuts import get_object_or_404
from django.db import models
from django.utils.translation import gettext_lazy as _
from products.models import Product, Category
from sales.models import Sale
from django.core.exceptions import ValidationError

TIMEZONES = (("Africa/Douala", "Cameroon"),)


class Settings(models.Model):
    logo = models.ImageField(
        verbose_name=_("Site Logo"), upload_to="settings", null=True, blank=True
    )
    company_name = models.CharField(
        verbose_name=_("Company Name"),
        max_length=255,
        null=True,
        blank=True,
        default="SOLIX",
    )
    timezone = models.CharField(
        verbose_name=_("Timezone"),
        max_length=30,
        choices=TIMEZONES,
        default="Africa/Douala",
        null=True,
        blank=True,
    )
    reorder_default = models.PositiveIntegerField(
        verbose_name=_("Re-Order Level"),
        help_text="Set reorder level for products without reorder level",
        default=1,
    )

    def __str__(self) -> str:
        return f"{self.company_name}"
