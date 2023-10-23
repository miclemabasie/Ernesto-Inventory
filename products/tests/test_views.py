from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product, Category
from django.contrib.auth import get_user_model

User = get_user_model()


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.product_list_url = reverse("products:list")
        self.user = User.objects.create_user(
            email="admin@mail.com",
            username="miclem",
            first_name="firstname",
            last_name="lastName",
            password="123Electron@3#",
        )
        self.user.save()

    def test_product_list_protected(self):
        response = self.client.get(reverse("products:list"))
        self.assertEqual(response.status_code, 302)

    def test_product_list_GET(self):
        self.client.login(email="admin@mail.com", password="123Electron@3#")
        response = self.client.get(self.product_list_url)
        self.assertEqual(response.status_code, 200)
