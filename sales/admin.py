from django.contrib import admin
from .models import Sale, SaleItem
from django.contrib.admin import TabularInline


class SaleItemInlineAdmin(admin.TabularInline):
    model = SaleItem
    extra = 6
    fields = ["product", "quantity", "unit_price", "total_price"]
    verbose_name = "Items part of this sale"
    can_delete = False


class SaleAdmin(admin.ModelAdmin):
    inlines = [
        SaleItemInlineAdmin,
    ]


admin.site.register(Sale, SaleAdmin)
