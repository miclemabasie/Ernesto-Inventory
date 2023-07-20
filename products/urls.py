from django.urls import path
from products import views

app_name = "products"
urlpatterns = [
    path("", views.product_list, name="list"),
    path("add-product/", views.products_add_view, name="add-product"),
    path("add-category/", views.category_add_view, name="add-category"),
    path("update/<int:product_id>/", views.update_product_view, name="update-product"),
    path("delete/<int:product_id>/", views.delete_product_view, name="delete-product"),
    path("detail/<int:product_id>/", views.product_detail_view, name="product-detail"),
]
