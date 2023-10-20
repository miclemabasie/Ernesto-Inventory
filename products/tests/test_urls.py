from django.test import SimpleTestCase, Client
from products.models import Product, Category
from products.views import (
    product_list,
    delete_category_view,
    product_detail_view,
    update_product_view,
    products_add_view,
    delete_product_view,
    category_edit_view,
    category_add_view,
)
from django.urls import resolve, reverse
from django.contrib.auth import get_user_model


class TestProductsUrls(SimpleTestCase):
    def test_product_list_url_resolves(sefl):
        url = reverse("products:list")
        url_function = resolve(url).func
        print("Testing only the products database")
        assert url_function == product_list

    def test_product_detail_url_resolves(self):
        url = reverse("products:product-detail", args=(1,))
        print(url)
        url_function = resolve(url).func
        assert url_function == product_detail_view

    def test_products_edit_url_resolves(self):
        url = reverse("products:update-product", args=(1,))
        url_function = resolve(url).func
        assert url_function == update_product_view

    def test_product_delete_url_resolves(self):
        url = reverse("products:delete-product", args=(1,))
        url_function = resolve(url).func
        assert url_function == delete_product_view

    def test_product_add_url_resolves(self):
        url = reverse("products:add-product")
        url_function = resolve(url).func
        assert url_function == products_add_view

    def test_category_add_url_resolves(self):
        url = reverse("products:add-category")
        url_function = resolve(url).func
        assert url_function == category_add_view

    def test_catetgory_delete_url_resolves(self):
        url = reverse("products:delete-category", args=(1,))
        url_function = resolve(url).func
        assert url_function == delete_category_view

    def test_category_edit_url_resolves(self):
        url = reverse("products:edit-category", args=(1,))
        url_function = resolve(url).func
        assert url_function == category_edit_view
