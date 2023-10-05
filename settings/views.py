from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Settings
from .forms import SettingsForm


def settings(request):
    template_name = "core/settings-home.html"
    setting = Settings.objects.all().first()
    if setting is None:
        setting = Settings()
    if request.method == "POST":
        # Set the settings for the form
        form = SettingsForm(request.POST, request.FILES, instance=setting)
        print(form)
        if form.is_valid():
            print(form)
            form.save()
            return redirect(reverse("home"))
        else:
            print("form is invalid")
            print(form.cleaned_data)
            print(form.errors)
    form = SettingsForm(instance=setting)
    context = {
        "form": form,
    }
    return render(request, template_name, context)
