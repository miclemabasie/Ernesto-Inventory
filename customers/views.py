from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Customer
from django.http import JsonResponse
import json
from .forms import CustomerAddForm
from django.contrib.auth.decorators import login_required


@login_required
def customer_list_view(request):
    customers = Customer.objects.all()
    form = CustomerAddForm()
    template_name = "customers/list.html"
    context = {
        "customers": customers,
        "customer_add_form": form,
    }

    return render(request, template_name, context)


@login_required
def customer_add_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # Create a new customer
        name = data["name"]
        phone = data["phone"]
        address = "None"
        email = "None"
        if data["address"]:
            address = data["address"]
        if data["email"]:
            email = data["email"]
        customer = Customer.objects.create(
            name=name, phone=phone, address=address, email="email"
        )
        # customer.save()

        data = {"status": "success", "message": "Customer created successfully!"}

        return JsonResponse(data)
    return redirect("customers:list")


@login_required
def edit_customer_view(request, customer_id):
    """
    Edit customer information
    """
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == "POST":
        form = CustomerAddForm(request.POST, instance=customer)
        if form.is_valid():
            # Save customer information and redirect user to customer list page
            form.save()
            return redirect("customers:list")
    # if the request is a GET, send the user to the edit page
    # prepolating the existing user information in the form form(instance=customer)
    form = CustomerAddForm(instance=customer)
    template_name = "customers/edit.html"
    context = {
        "customer": customer,
        "customer_add_form": form,
    }
    return render(request, template_name, context)
