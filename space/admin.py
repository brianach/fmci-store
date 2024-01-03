from django.contrib import admin
from .models import Labspace, Deskspace, Space

# Register your models here.


class SpaceAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class PricingMixin:
    def pricing(self, obj):
        # Assuming 'termprices' is a JSONField
        pricing_info = obj.termprices

        # Define keys and default value
        keys = ['a', 'b', 'c', 'd']
        default_value = None

        # Create a list to store values for each key
        pricing_columns = [pricing_info.get(
            key, default_value) for key in keys]

        # Convert the list to a string
        pricing_string = ', '.join(str(column) for column in pricing_columns)

        return pricing_string

    pricing.short_description = 'Pricing'


class LabspaceAdmin(PricingMixin, admin.ModelAdmin):
    list_display = ('sku', 'name', 'pricing')


class DeskspaceAdmin(PricingMixin, admin.ModelAdmin):
    list_display = ('sku', 'name', 'pricing')


admin.site.register(Space, SpaceAdmin)
admin.site.register(Labspace, LabspaceAdmin)
admin.site.register(Deskspace, DeskspaceAdmin)
