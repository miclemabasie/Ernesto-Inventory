from django.urls import path
from . import views

app_name = "commons"

urlpatterns = [
    path("import_data/", views.import_data, name="import_data"),
    path("export_data/", views.export_data, name="export_data"),
]
