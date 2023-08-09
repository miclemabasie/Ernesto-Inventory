from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .decorators import require_post
from .forms import ProductAddForm, CategoryAddForm
import json
from django.utils.text import slugify
from django.urls import reverse
from django.core.exceptions import ValidationError
from sales.models import SaleItem
from django.db.models import Sum


@login_required
def home_view(request):
    template_name = "core/home.html"
    sales_data = SaleItem.objects.values("created__month").annotate(
        total_price=Sum("price")
    )
    context = {
        "section": "home",
        "sales_data": sales_data,
    }
    return render(request, template_name, context)


@login_required
def product_list(request):
    template_name = "products/list.html"
    products = Product.objects.all()
    product_add_form = ProductAddForm()
    category_add_form = CategoryAddForm()
    categories = Category.objects.all()
    context = {
        "section": "Products",
        "products": products,
        "categories": categories,
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
    product.save()
    data = {
        "status": "success",
        "message": f"Succes: {product.name} added to {product.category.name}!",
    }
    return JsonResponse(data)


@login_required
def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    template_name = "products/detail.html"
    context = {
        "product": product,
    }
    return render(request, template_name, context)


@login_required
def update_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductAddForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(f"/products/?updatedproduct={product_id}")
            # return redirect(reverse("products:list"))
        else:
            print("#$###########3", form.errors)
            raise ValidationError("Invalid product data")
    form = ProductAddForm(instance=product)
    template_name = "products/update.html"
    context = {
        "product": "product",
        "product_form": form,
    }
    return render(request, template_name, context)


@login_required
def delete_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # reqeust to delete product
    product.delete()
    return redirect(reverse("products:list"))


@login_required
@require_post
def category_add_view(request):
    print("Request to add")
    data = json.loads(request.body)
    category_name = data["name"]

    # Check if category with same name alread exists
    try:
        category = Category.objects.get(name__iexact=category_name)
        return JsonResponse(
            {"status": "Error", "message": "Category with this name already exist!"}
        )
    except Category.DoesNotExist:
        pass
    # Create the category
    category = Category(name=category_name)
    category.slug = slugify(category_name)
    category.save()
    data = {
        "status": "success",
        "message": "Category added successfuly",
    }
    return JsonResponse(data)


@login_required
def category_edit_view(request, category_id):
    print(f"This is the cat id: @####", category_id)
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = CategoryAddForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect(reverse("products:list"))
        print("#########33", form.errors)
    form = CategoryAddForm(instance=category)
    template_name = "products/category_edit.html"
    context = {
        "category_form": form,
    }
    return render(request, template_name, context)


@login_required
def delete_category_view(request, category_id):
    cateogry = get_object_or_404(Category, id=category_id)
    # reqeust to delete product
    cateogry.delete()
    return redirect(reverse("products:list"))
