from django.contrib import admin
from .models import Store, Category

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image_one',
        'image_two',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)