from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from products.models import Product
from .utils import generate_transactionID
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Sum

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
        return f"saleitem"

    def SaleAnaylisData(self, step):
        data = []
        # Get all sales Items whose sales are validated
        saleitems_length = SaleItem.objects.filter(sale__validated=True).count()
        start = 0
        today = datetime.now().date()
        # Calculate the start and end dates for the last 14 days
        end_date = today
        for i in range(start, saleitems_length, step):
            start_date = today - timedelta(days=step)
            print(start_date)
            # Query the sales data within the last 14 days and calculate the sum of prices
            sales_data = SaleItem.objects.filter(created__range=[start_date, end_date])
            print(sales_data)
            total_price = sales_data.aggregate(total=Sum("unit_price"))
            print("Total Price: ", total_price)
            data.append(total_price["total"])
            print("data: ", data)
            today = today - timedelta(days=1)

            print("########################## today: ", today)
        return data


class Sale(models.Model):
    transaction_id = models.CharField(
        verbose_name=_("Transaction ID"), max_length=250, null=True, blank=True
    )
    sales_man = models.ForeignKey(
        User, related_name="sales", on_delete=models.SET_NULL, null=True
    )
    total_sale_price = models.FloatField(default=0.0, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    validated = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # calculate and set the total cost of the sale
        # get all saleItems for this sale
        total_cost = 0
        if self.validated == True:
            saleItems = SaleItem.objects.filter(sale__id=self.id)
            if len(saleItems) > 0:
                for item in saleItems:
                    total_cost += item.total_price
            self.transaction_id = generate_transactionID()
            self.total_sale_price = total_cost
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.transaction_id}-{self.date_created}"


from django.db.models import Sum
from django.views import View
from django.http import JsonResponse
from .models import Sale


class SaleDataView(View):
    def get(self, request):
        # Group sales by month and calculate total price for each month
        sales_data = Sale.objects.values("created__month").annotate(
            total_price=Sum("price")
        )

        # Create a list of total prices
        prices_list = [item["total_price"] for item in sales_data]

        return JsonResponse(prices_list, safe=False)
