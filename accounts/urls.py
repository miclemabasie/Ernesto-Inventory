from django.urls import path
from accounts import views

app_name = "accounts"


urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("users/", views.list_users, name="list"),
    path("add_user/", views.add_user, name="add_user"),
    path("edit_user/<str:username>/", views.edit_user, name="edit_user"),
]
