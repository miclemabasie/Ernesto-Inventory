from django.urls import path
from products import views

app_name = "products"
urlpatterns = [
    path("", views.product_list, name="list"),
    path("add-product/", views.products_add_view, name="add-product"),
    path("update/<int:product_id>/", views.update_product_view, name="update-product"),
    path("delete/<int:product_id>/", views.delete_product_view, name="delete-product"),
    path("detail/<int:product_id>/", views.product_detail_view, name="product-detail"),
    # Category
    path("add-category/", views.category_add_view, name="add-category"),
    path(
        "edit-category/<int:category_id>/",
        views.category_edit_view,
        name="edit-category",
    ),
    path(
        "delete-category/<int:category_id>/",
        views.delete_category_view,
        name="delete-category",
    ),
    path(
        "export_porducts_to_csv/",
        views.export_product_data,
        name="export_porducts_to_csv",
    ),
]
