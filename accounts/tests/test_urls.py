from django.test import TestCase
from django.urls import resolve
from customers.views import (
    customer_list_view,
    edit_customer_view,
    send_message,
    customer_add_view,
)
from django.urls import reverse
from customers.models import Customer

# Using simpletestcase when we dont need to interact with the database.


class TestUrls(TestCase):
    def setUp(self):
        # Create a customer in the database
        self.customer = Customer.objects.create(
            name="miclem", phone="34343434", address="Bambili", email="miclem@mail.com"
        )
        self.customer.save()

    def test_customer_list_url_resolves(self):
        # get the url
        url = reverse("customers:list")
        # grab the fucntion associated to that url
        url_function = resolve(url).func
        assert url_function == customer_list_view

    def test_edit_customer_url_resolves(self):
        url = reverse("customers:customer-edit-view", args=(self.customer.id,))
        url_function = resolve(url).func
        assert url_function == edit_customer_view

    def test_send_message_url_resolves(self):
        url = reverse("customers:send_message", args=(self.customer.id,))
        url_function = resolve(url).func
        assert url_function == send_message

    def test_add_customer_url_resolves(self):
        url = reverse("customers:add-customer-view")
        url_function = resolve(url).func
        assert url_function == customer_add_view
