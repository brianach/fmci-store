from django.shortcuts import render
from .models import Service, Compute, Digital


def services(request):
    services = Service.objects.all()
    compute = Compute.objects.all()
    digital = Digital.objects.all()

    return render(request, 'service/service.html', {
        'services': services,
        'compute': compute,
        'digital': digital, }
    )
