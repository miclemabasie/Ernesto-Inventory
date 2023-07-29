from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Customer(models.Model):
    name = models.CharField(verbose_name=_("Customer's Name"), max_length=200)
    phone = models.CharField(verbose_name=_("Phone Number"), max_length=200)
    address = models.CharField(
        verbose_name=_("Address"), max_length=200, null=True, blank=True
    )
    email = models.EmailField(verbose_name=_("Email"), null=True, blank=True)
