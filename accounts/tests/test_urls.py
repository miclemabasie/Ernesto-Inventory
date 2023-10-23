from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import login_view, list_users, add_user, edit_user


class TestUrlsResolve(SimpleTestCase):
    def test_login_url_resolves(self):
        login_func = resolve(reverse("accounts:login")).func

        assert login_func == login_view

    def test_users_list_url_resolves(sefl):
        user_list_url = reverse("accounts:list")
        user_list_func = resolve(user_list_url).func
        assert user_list_func == list_users

    def test_add_user_url_resolves(self):
        add_user_url = reverse("accounts:add_user")
        add_user_func = resolve(add_user_url).func
        assert add_user_func == add_user

    def test_user_edit_url_resolves(self):
        edit_user_url = reverse("accounts:edit_user", args=("username",))
        edit_user_func = resolve(edit_user_url).func
        assert edit_user_func == edit_user
