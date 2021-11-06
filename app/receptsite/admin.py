from django.contrib import admin
from receptsite.models import Bludo, Ingredient

# Register your models here.

@admin.register(Bludo)
class ViewPageBludoAdmin(admin.ModelAdmin):

    list_display = (
        "image",
        "nazvanie",
        "prigotovlenie",
    )

    search_fields = (
        "nazvanie",
        "prigotovlenie",
    )

    ordering = ("nazvanie",)


@admin.register(Ingredient)
class ViewPageBludoAdmin(admin.ModelAdmin):

    list_display = (
        "nazvanie",
    )

    search_fields = (
        "nazvanie",
    )

    ordering = ("nazvanie",)