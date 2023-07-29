from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "email", "address"]


admin.site.register(Customer, CustomerAdmin)
