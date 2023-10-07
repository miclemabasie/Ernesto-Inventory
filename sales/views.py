from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Sale, SaleItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
import json
from .forms import SaleItemForm
from products.decorators import require_post
from products.models import Product
from django.views.decorators.csrf import csrf_exempt
from openpyxl import Workbook
from datetime import datetime


@login_required
def sale_list(request):
    sales = SaleItem.objects.filter(sale__validated=True)
    sale_form = SaleItemForm(request.POST or None)
    context = {
        "saleItems": sales,
        "sale_form": sale_form,
    }
    template_name = "sales/list.html"
    return render(request, template_name, context)


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

    # Check if the request is carrying a query parameter
    # for validating the existing sale object
    validate_query = request.GET.get("query")
    if validate_query == "validateSale":
        # validate the existing sale
        sale.validated = True
        sale.save()

        # adjust product's quantities
        # !!! should be transfered to the sale save method in the models
        productSales = sale.saleitems.all()
        for saleItem in productSales:
            saleItem.product.quantity -= int(saleItem.quantity)
            saleItem.product.save()
            print("This is save", saleItem.product)

        return redirect(reverse("sales:list"))
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

    # Check if quantity of product is Greater or equal to quantity about to be sold
    if product.quantity < int(quantity):
        print("#############", product.quantity, quantity)
        data = {
            "status": "warnine",
            "message": "No enough products to perform this transaction",
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
        "totalPrice": sale_item_obj.total_price,
        "saleID": sale.id,
        "saleitem_id": sale_item_obj.id,
    }
    return JsonResponse(data)


@login_required
def sale_detail(request, saleitem_id):
    template_name = "sales/details.html"
    sale = get_object_or_404(SaleItem, id=saleitem_id)
    sold_with_products = SaleItem.objects.filter(
        sale__transaction_id=sale.sale.transaction_id
    )
    # remove the main sale from the sold with products list
    products = []
    for saleItem in sold_with_products:
        if saleItem.product.id != sale.product.id:
            products.append(saleItem)
    context = {
        "sale": sale,
        "products_with": products,
    }
    return render(request, template_name, context)


@csrf_exempt
@login_required
def remove_sale_previewItem(request):
    """
    Remove item in the front end preview table in the
    database when user clicks on 'x' button.
    """
    data = json.loads(request.body)
    saleItem_id = data["deleteSaleID"]
    # get the item from the database
    try:
        saleItem = get_object_or_404(SaleItem, id=saleItem_id)
        saleItem.delete()
        data = {
            "status": "success",
            "message": f"saleItem ID No. {saleItem_id} removed.",
        }
        return JsonResponse(data)
    except SaleItem.DoesNotExist:
        data = {"status": "error", "message": "No saleItem with given id found!"}
        return JsonResponse(data)


def delete_sale(request, sale_id):
    """
    Delete a saleItem from the database.
    """
    sale = get_object_or_404(SaleItem, id=sale_id)
    sale.delete()
    return redirect(reverse("sales:list"))


def edit_sale(request, sale_id):
    """
    Edit saleItem
    """
    sale = get_object_or_404(SaleItem, id=sale_id)
    oldSaleQuantity = int(sale.quantity)
    product = sale.product
    if request.method == "POST":
        form = SaleItemForm(request.POST, instance=sale)
        if form.is_valid():
            saleItem = form.save(commit=False)
            # adjust prouducts quantity
            newSaleQuantity = int(saleItem.quantity)
            print("old", oldSaleQuantity, " new: ", newSaleQuantity)
            if oldSaleQuantity != newSaleQuantity:
                print("changing quantity")
                # sale quantity has been updated
                if newSaleQuantity < oldSaleQuantity:
                    diff = oldSaleQuantity - newSaleQuantity
                    product.quantity += diff
                    product.save()
                elif newSaleQuantity > oldSaleQuantity:
                    # quantity has been added for the sale
                    diff = newSaleQuantity - oldSaleQuantity
                    product.quantity -= diff
                    product.save()
            saleItem.save()

            return redirect(reverse("sales:list"))
        else:
            print(form.errors)
            if (
                "Quantity can not be greater than available product quantity!"
                in form.errors["__all__"][0]
            ):
                error = form.errors["__all__"][0]
            template_name = "sales/edit.html"
            context = {
                "sale_form": form,
                "errors": error,
            }
            return render(request, template_name, context)

    form = SaleItemForm(instance=sale)
    template_name = "sales/edit.html"
    context = {
        "sale_form": form,
    }
    return render(request, template_name, context)


def handle_product_return(request, sale_id):
    """
    Handling products returned by customer after being bougth
    """
    # Get the sale item with the sale id
    sale_item = get_object_or_404(Sale, id=sale_id)
    # print out all the products in the sale item
    for product in sale_item:
        print(product)

    template_name = "sales/return_products.html"
    context = {
        "page": "Returned Products",
    }
    return render(request, template_name, context)
