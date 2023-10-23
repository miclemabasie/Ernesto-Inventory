from django.test import TestCase, Client
from django.urls import resolve, reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class TestAccountsViews(TestCase):
    def setUp(self):
        user_a = User.objects.create_user(
            email="test@mail.com",
            username="testuser",
            first_name="fName",
            last_name="lName",
            password="123Testing3#",
        )
        user_a.save()
        self.user_a = user_a

    def test_user_exists(self):
        users = User.objects.all()
        user_count = users.count()
        user = users.first()
        self.assertEqual(user_count, 1)
        self.assertTrue(self.user_a.check_password("123Testing3#"))

    def test_login_view(self):
        response = self.client.get(reverse("accounts:login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/authentication/login.html")

    def test_login_view_post(self):
        # Test that user can login successfuly with correct credentials
        login_url = reverse("accounts:login")
        data = {"email": "test@mail.com", "password": "123Testing3#"}
        response = self.client.post(login_url, data, follow=True)
        login_redirect = "/"
        self.assertEqual(response.request["PATH_INFO"], login_redirect)
        self.assertEqual(response.status_code, 200)

    def test_login_view_POST_wrong_credentials(self):
        login_url = reverse("accounts:login")
        data = {"email": "userb@mail.com", "password": "123Testing3#"}
        response = self.client.post(login_url, data, follow=True)
        login_redirect = "/accounts/login/"
        self.assertEqual(response.request["PATH_INFO"], login_redirect)
        self.assertEqual(response.status_code, 200)
