from django.shortcuts import render
from .models import Product, Category
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    template_name = "core/home.html"
    context = {"section": "home"}
    return render(request, template_name, context)
