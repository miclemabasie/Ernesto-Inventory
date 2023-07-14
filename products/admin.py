from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created", "updated"]
    list_filter = ["created"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "price", "quantity", "reorder_level", "active"]
    list_filter = ["category", "price", "active"]
    list_per_page = 25
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name", "category"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
