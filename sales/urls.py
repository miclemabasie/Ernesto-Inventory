from django.urls import path
from sales import views

app_name = "sales"
urlpatterns = [
    path("", views.sale_list, name="list"),
    path("<int:saleitem_id>/", views.sale_detail, name="sale-detail"),
    path("add-sale", views.add_sale_view, name="add-sale"),
    path(
        "remove-sale-preview", views.remove_sale_previewItem, name="remove_preview_item"
    ),
    path("delete-sale/<int:sale_id>/", views.delete_sale, name="sale-delete"),
    path("edit/<int:sale_id>/", views.edit_sale, name="sale-edit"),
]
