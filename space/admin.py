from django.contrib import admin
from .models import Labspace, Deskspace, Space

# Register your models here.


class SpaceAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name',)


class PricingMixin:
    def get_pricing_columns(self, obj):
        # Assuming 'pricing' is a JSONField
        pricing_info = obj.pricing

        # Define keys and default value
        keys = ['a', 'b', 'c', 'd']
        default_value = None

        # Create a list to store values for each key
        pricing_columns = []

        for key in keys:
            pricing_columns.append(pricing_info.get(key, default_value))

        return pricing_columns

    def display_pricing(self, obj):
        return self.get_pricing_columns(obj)

    display_pricing.short_description = 'Pricing'


class LabspaceAdmin(PricingMixin, admin.ModelAdmin):
    list_display = ('sku', 'name', 'display_pricing')


class DeskspaceAdmin(PricingMixin, admin.ModelAdmin):
    list_display = ('sku', 'name', 'display_pricing')


admin.site.register(Space, SpaceAdmin)
admin.site.register(Labspace, LabspaceAdmin)
admin.site.register(Deskspace, DeskspaceAdmin)
