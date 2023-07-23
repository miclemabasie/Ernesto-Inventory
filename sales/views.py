from django.shortcuts import render
from .models import Sale, SaleItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from .forms import SaleItemForm


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


@login_required
def add_sale_view(request):
    user = request.user
    # create a new sale
    sale = Sale()
    if request.method == "POST":
        # Get sale item data
        sale_item_data = json.loads(request.body)
        # create a new sale item


@login_required
def sale_detail(request, saleitem_id, transaction_id):
    template_name = "sales/details.html"
    context = {}
    return render(request, template_name, context)
