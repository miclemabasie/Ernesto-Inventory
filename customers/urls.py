from django.urls import path
from customers import views


app_name = "customers"


urlpatterns = [
    path("", views.customer_list_view, name="list"),
    path(
        "edit/<int:customer_id>/", views.edit_customer_view, name="customer-edit-view"
    ),
    path("add-customer/", views.customer_add_view, name="add-customer-view"),
]
