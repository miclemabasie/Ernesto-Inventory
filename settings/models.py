from django.db import models
from django.utils.translation import gettext_lazy as _
from products.models import Product, Category
from sales.models import Sale
from django.core.exceptions import ValidationError


class Settings(models.Model):
    logo = models.ImageField(
        verbose_name=_("Site Logo"), upload_to="settings", null=True, blank=True
    )
    company_name = models.CharField(
        verbose_name=_("Company Name"), max_length=255, null=True, blank=True
    )
    timezone = models.CharField(
        verbose_name=_("Timezone"), max_length=30, null=True, blank=True
    )
    reoder_default = models.PositiveIntegerField(
        verbose_name=_("Re-Order Level"),
        help_text="Set reorder level for products without reorder level",
    )

    def __str__(self) -> str:
        return f"{self.company_name}"

    def save(self, *args, **kwargs):
        # Try to get a settings from the database
        # Note: only one settings intance can exist
        setting = Settings.objects.get(id=1)
        if setting:
            raise ValidationError("Settings module already Exist!")
        super().save(*args, **kwargs)
