from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm, ProfileForm, CustomUserChangeForm
from django.contrib.auth.decorators import permission_required
from .models import Profile

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


def logout_view(request):
    context = {}
    logout(request)
    return redirect("/")


@login_required
@permission_required("accounts.view_user")
def list_users(request):
    # if request.user.has_perm("accounts.view_user"):
    users = User.objects.filter(is_active=True)
    template_name = "accounts/list_users.html"
    context = {
        "users": users,
    }

    return render(request, template_name, context)
    # else:
    #     return HttpResponse("Not allowed for you!")


@login_required
@permission_required("accounts.add_user", "accounts.change_user")
def add_user(request):
    form = CustomUserCreationForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    if request.method == "POST":
        print("The form was posted")
        if form.is_valid():
            data = form.cleaned_data
            profile_image = request.FILES.get("image")
            phone = request.POST.get("phone")
            user_group = request.POST["grouptype"]
            # Get the group matching group type
            try:
                group = Group.objects.get(name=user_group)
            except Group.DoesNotExist:
                # Assing user to sales man by default
                group = Group.objects.get(name="sales_men")

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
            # Create a profile for the user aswell

            profile = Profile.objects.create(
                user=user, image=profile_image, phone=phone
            )
            profile.save()
            return redirect(reverse("home"))
        else:
            print(form.errors)
    template_name = "accounts/add_user.html"
    context = {"form": form, "profile_form": profile_form}
    return render(request, template_name, context)


@login_required
@permission_required("accounts.change_user")
def edit_user(request, username):
    user = get_object_or_404(User, username=username)
    form = CustomUserChangeForm(request.POST or None, instance=user)
    # Get the user's profile
    profile = user.profile
    profile_form = ProfileForm(request.POST or None, instance=profile)
    if request.method == "POST":
        if profile_form.is_valid() and form.is_valid():
            form.save()
            print("form is saved")
            return redirect(reverse("home"))
        else:
            print("ERRORS::: ###########")
            print(form.errors)
            print(profile_form.errors)
        # get profile associated with user
    template_name = "accounts/edit_user.html"
    context = {
        "username": user.username,
        "form": form,
        "profile_form": profile_form,
    }
    return render(request, template_name, context)
