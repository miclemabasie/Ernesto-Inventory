from django.shortcuts import render
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .decorators import require_post
from .forms import ProductAddForm, CategoryAddForm
import json
from django.utils.text import slugify


@login_required
def home_view(request):
    template_name = "core/home.html"
    context = {"section": "home"}
    return render(request, template_name, context)


@login_required
def product_list(request):
    template_name = "products/list.html"
    products = Product.objects.all()
    product_add_form = ProductAddForm()
    category_add_form = CategoryAddForm()
    context = {
        "section": "Products",
        "products": products,
        "product_form": product_add_form,
        "category_form": category_add_form,
    }

    return render(request, template_name, context)


@login_required
@require_post
def products_add_view(request):
    # Get the data sent from javascript
    data = json.loads(request.body)
    name = data["name"]
    category = data["category"]
    price = data["price"]
    quantity = data["quantity"]
    reorder_level = data["reorder_level"]
    # Try to get the category object of using the given category id
    try:
        category = Category.objects.get(id=category)
    except Category.DoesNotExist:
        return JsonResponse({"message": "invalid Category", "status": "error"})
    # Create a new product with data obj
    product = Product(
        name=name,
        category=category,
        price=price,
        quantity=quantity,
        reorder_level=reorder_level,
    )

    # Check if product already exists with same name
    try:
        test_product = Product.objects.get(name__iexact=name)
        if test_product:
            return JsonResponse(
                {"message": "Product with this name already exists", "status": "error"}
            )
    except Product.DoesNotExist:
        pass

    # Set the user to the current logged in user
    product.user = request.user
    # Set active to the product if quantity is greater than 0
    if int(product.quantity) < 0:
        product.active = False
    # product.save()
    data = {
        "status": "success",
        "message": f"Succes: {product.name} added to {product.category.name}!",
    }
    return JsonResponse(data)
