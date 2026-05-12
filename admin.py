from django.apps import AppConfig
from django.contrib import admin

# Register your models here.
class AdminConfig(AppConfig):
    name = 'gondon'


# admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "image_preview"]
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="150" height="150" '
                'style="object-fit: cover; border-radius: 8px;" />',
                obj.image.url
            )
        return "Rasm yo'q"

    image_preview.short_description = "Rasm"


