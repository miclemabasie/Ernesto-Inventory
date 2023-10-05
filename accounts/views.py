from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import permission_required


User = get_user_model()


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


@login_required
def list_users(request):
    users = User.objects.filter(is_active=True)
    template_name = "accounts/list_users.html"
    context = {
        "users": users,
    }

    return render(request, template_name, context)


@login_required
@permission_required("accounts.add_user", "accounts.change_user")
def add_user(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == "POST":
        print("The form was posted")
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user_group = request.POST["grouptype"]
            # Get the group matching group type
            group = Group.objects.get(name=user_group)
            email = data["email"]
            username = data["username"]
            first_name = data["first_name"]
            last_name = data["last_name"]
            password = data["password1"]
            user = User(
                email=email,
                username=username,
                first_name=first_name,
                last_name=last_name,
            )
            user.is_superuser = False
            user.is_staff = False

            user.set_password(password)
            if user_group == "business_administrator":
                user.is_staff = True
            user.save()
            user.groups.add(group)
            user.save()
            return redirect(reverse("home"))
        else:
            print(form.errors)
    template_name = "accounts/add_user.html"
    context = {
        "form": form,
    }
    return render(request, template_name, context)


{
    "email": "test@mail.com",
    "username": "tester",
    "first_name": "testing",
    "last_name": "testee",
    "password1": "12electron@3#",
    "password2": "12electron@3#",
}
