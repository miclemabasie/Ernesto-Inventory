from django.shortcuts import render
from .models import Product, Category
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    template_name = "core/home.html"
    context = {"section": "home"}
    return render(request, template_name, context)


@login_required
def product_list(request):
    template_name = "products/list.html"
    products = Product.objects.all()
    context = {
        "page_title": "Products",
        "products": products,
    }

    return render(request, template_name, context)
