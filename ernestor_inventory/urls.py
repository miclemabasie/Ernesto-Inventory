from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("products/", include("products.urls", namespace="products")),
    path("sales/", include("sales.urls", namespace="sales")),
    path("customers/", include("customers.urls", namespace="customers")),
    path("settings/", include("settings.urls", namespace="settings")),
    path("commons/", include("commons.urls", namespace="commons")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
