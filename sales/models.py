from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from products.models import Product

User = get_user_model()


class SaleItem(models.Model):
    product = models.ForeignKey(
        Product, related_name="sale_items", on_delete=models.SET_NULL, null=True
    )
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))
    unit_price = models.FloatField(
        help_text="In XAF",
        default=0.00,
        null=True,
        blank=True,
    )
    total_price = models.FloatField(
        help_text="In XAF",
        default=0.00,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        # set the price of the sale item
        if not self.unit_price:
            self.unit_price = self.product.price
        self.total_price = self.unit_price * self.quantity
        return super.save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.product.name} sold"


class Sale(models.Model):
    transaction_id = models.CharField(verbose_name=_("Transaction ID"), max_length=250)
    sales_man = models.ForeignKey(
        User, related_name="sales", on_delete=models.SET_NULL, null=True
    )
    items = models.ManyToManyField(SaleItem)
    quantity = models.PositiveIntegerField(default=0)
    total_sale_price = models.FloatField(default=0.0)
    date_created = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        # calculate and set the total cost of the sale
        total_cost = 0
        for item in self.items.all():
            total_cost += item.unit_price
        self.total_sale_price = total_cost
        return super.save(*args, **kwargs)
