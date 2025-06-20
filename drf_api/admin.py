from django.contrib import admin

from .models import Item


# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "created_at")
    search_fields = ("name", "description")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
