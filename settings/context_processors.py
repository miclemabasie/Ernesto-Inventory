from .models import Settings


def site_settings(request):
    setting = Settings.objects.all().first()

    context = {"site_settings": setting}
    return context
