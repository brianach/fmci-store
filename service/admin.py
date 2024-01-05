from django.contrib import admin
from .models import Compute, Digital, Service

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class BaseserviceAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'description', 'item_1',
                    'item_2', 'item_3', 'item_4')


class ComputeserviceAdmin(BaseserviceAdmin):
    pass


class DigitalserviceAdmin(BaseserviceAdmin):
    pass


admin.site.register(Service, ServiceAdmin)
admin.site.register(Compute, ComputeserviceAdmin)
admin.site.register(Digital, DigitalserviceAdmin)
