from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from products.models import Product
from .utils import generate_transactionID
from django.utils import timezone


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
    sale = models.ForeignKey("Sale", related_name="saleitems", on_delete=models.CASCADE)
    created = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # set the price of the sale item
        if not self.unit_price:
            self.unit_price = self.product.price
        self.total_price = float(self.unit_price) * int(self.quantity)
        if not self.created:
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.product.name} sold"


class Sale(models.Model):
    transaction_id = models.CharField(
        verbose_name=_("Transaction ID"), max_length=250, null=True, blank=True
    )
    sales_man = models.ForeignKey(
        User, related_name="sales", on_delete=models.SET_NULL, null=True
    )
    total_sale_price = models.FloatField(default=0.0, null=True, blank=True)
    date_created = models.DateTimeField(blank=True, null=True)
    validated = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # calculate and set the total cost of the sale
        # get all saleItems for this sale
        total_cost = 0
        if self.validated == True:
            saleItems = SaleItem.objects.get(sale__transaction_id=self.transaction_id)
            if len(saleItems) > 0:
                for item in saleItems:
                    total_cost += item.total_price
            self.transaction_id = generate_transactionID()
        return super().save(*args, **kwargs)
