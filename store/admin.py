from django.contrib import admin
from .models import StoreItem, Category

# Register your models here.


class StoreItemAdmin(admin.ModelAdmin):
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
        'pk',
    )


admin.site.register(StoreItem, StoreItemAdmin)
admin.site.register(Category, CategoryAdmin)
