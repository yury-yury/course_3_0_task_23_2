from typing import Tuple
from django.contrib import admin

from catalog.models import Category, Product, Contact


class CategoryAdmin(admin.ModelAdmin):
    """
    The CategoryAdmin class inherits from the ModelAdmin class. Defines the output of instance fields
    to the administration panel and the ability to edit them.
    """
    list_display: Tuple[str, ...] = ("id", "name")
    list_display_links: Tuple[str, ...] = ("id", "name")


class ProductAdmin(admin.ModelAdmin):
    """
    The ProductAdmin class inherits from the ModelAdmin class. Defines the output of instance fields
    to the administration panel and the ability to edit them.
    """
    list_display: Tuple[str, ...] = ("id", "name", "price", "category")
    list_display_links: Tuple[str, ...] = ("id", "name")
    readonly_fields: Tuple[str, ...] = ("id", "created_at", "updated_at")
    search_fields: Tuple[str, ...] = ("name", "description")
    list_filter: Tuple[str, ...] = ("category", )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact)
