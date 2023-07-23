from django.shortcuts import render
from .models import Sale, SaleItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json


@login_required
def add_sale_view(request):
    user = request.user
    # create a new sale
    sale = Sale()
    if request.method == "POST":
        # Get sale item data
        sale_item_data = json.loads(request.body)
