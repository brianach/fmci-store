from django.contrib import admin
from .models import Labspace, Deskspace, Space

# Register your models here.


class SpaceAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class BasespaceAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'description', 'price_a',
                    'price_b', 'price_c', 'price_d')


class LabspaceAdmin(BasespaceAdmin):
    pass


class DeskspaceAdmin(BasespaceAdmin):
    pass


admin.site.register(Space, SpaceAdmin)
admin.site.register(Labspace, LabspaceAdmin)
admin.site.register(Deskspace, DeskspaceAdmin)
