from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate


def login_view(request):
    context = {}
    template_name = "accounts/authentication/login.html"
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # extract username and password
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            # Authenticate the user // check if user exist
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect(reverse("home"))
            else:
                pass
    context["form"] = form
    return render(request, template_name, context)
