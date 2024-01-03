from django.contrib import admin
from .models import Labspace, Deskspace, Space

# Register your models here.


class SpaceAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class LabspaceAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'term',
        'price',
    )


class DeskspaceAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'term',
        'price',
    )


admin.site.register(Space, SpaceAdmin)
admin.site.register(Labspace, LabspaceAdmin)
admin.site.register(Deskspace, DeskspaceAdmin)
