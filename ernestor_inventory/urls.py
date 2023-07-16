from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("", home_view, name="home"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, doccument_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, doccument_root=settings.MEDIA_ROOT)
