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
    # Dict to map each month to a list which contains [0] => its month number, [1] => its total sales value
    data = {
        "Jan": [1, 0],
        "Feb": [2, 0],
        "Mar": [3, 0],
        "Apr": [4, 0],
        "May": [5, 0],
        "Jun": [6, 0],
        "Jul": [7, 0],
        "Aug": [8, 0],
        "Sep": [9, 0],
        "Oct": [10, 0],
        "Nov": [11, 0],
        "Dec": [12, 0],
    }

    for k, v in data.items():
        for i in range(len(sales_data)):
            if v[0] == sales_data[i]["created__month"]:
                data[k][1] = sales_data[i]["total_price"]

    for k, v in data.items():
        data[k] = v[1]
    months = list(data.keys())
    values = list(data.values())

    data = {"labels": months, "values": values}
    return data
