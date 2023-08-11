from sales.models import SaleItem
from django.db.models import Sum
from collections import deque


def get_sales_data(period):
    """
    Retrieves sales data to be used by chart js in the frontend
    this data is retrieved based on the period provided (month, week, day)
    This data is grouped based on the given peroid and the total number number of sales for each
    grouping is returned by the function
    """
    sales_data = SaleItem.objects.values(f"created__{period}").annotate(
        total_price=Sum("total_price")
    )
    # convert the queryset into a list
    sales_data = list(sales_data)

    total_prices = deque()
    print("############### sales data", sales_data)
    for _ in sales_data:
        total_prices.appendleft(_["total_price"])
    return list(total_prices)
