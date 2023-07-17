from django.urls import path
from products import views

app_name = "products"
urlpatterns = [
    path("", views.product_list, name="list"),
    path("add-product/", views.products_add_view, name="add-product"),
]
