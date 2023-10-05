from django.urls import path
from accounts import views

app_name = "accounts"


urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("users/", views.list_users, name="list"),
    path("add_user/", views.add_user, name="add_user"),
]
