from products.models import Product
from sales.models import SaleItem
from customers.models import Customer


def total_products(request):
    total = Product.objects.all().count()
    context = {"total_products": total}
    return context


def total_customers(request):
    total = Customer.objects.all().count()
    context = {"total_customers": total}
    return context


def total_sales(request):
    total = SaleItem.objects.all().count()
    context = {"total_sales": total}
    return context
