from django.shortcuts import render
from .models import Sale, SaleItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from .forms import SaleItemForm
from products.decorators import require_post
from products.models import Product


@login_required
def sale_list(request):
    sales = SaleItem.objects.all()
    sale_form = SaleItemForm(request.POST or None)
    context = {
        "sales": sales,
        "sale_form": sale_form,
    }
    template_name = "sales/list.html"
    return render(request, template_name, context)


# @require_post
@login_required
def add_sale_view(request):
    user = request.user

    data = json.loads(request.body)
    # Check if a sale was previously create
    sale_id = data["saleID"]
    if not data["saleID"]:
        # create a new sale
        sale = Sale(sales_man=user)
        sale.save()
    else:
        sale = Sale.objects.get(id=sale_id)
    # Get sale item data
    # Extract data from javascriptData
    {
        "product": "3",
        "quantity": "5",
        "price": "456",
        "tPrice": "",
        "date": "2023-07-12",
    }
    productID = data["product"]
    quantity = data["quantity"]
    price = data["price"]
    tPrice = data["tPrice"]
    created = data["date"]
    # get associated product
    try:
        product = Product.objects.get(id=productID)
    except Product.DoesNotExist:
        data = {
            "status": "warnine",
            "message": "No product found with given ID",
        }
        return JsonResponse(data)
    # create a new saleItem element with extracted data
    sale_item_obj = SaleItem(
        product=product, quantity=quantity, unit_price=price, sale=sale, created=created
    )
    sale_item_obj.save()

    data = {
        "status": "success",
        "message": "saleitem successfully added",
        "product": sale_item_obj.product.name,
        "quantity": sale_item_obj.quantity,
        "price": sale_item_obj.unit_price,
        "saleID": sale.id,
    }
    return JsonResponse(data)


@login_required
def sale_detail(request, saleitem_id, transaction_id):
    template_name = "sales/details.html"
    context = {}
    return render(request, template_name, context)
