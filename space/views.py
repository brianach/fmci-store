from django.shortcuts import render
from .models import Space, Labspace, Deskspace


def spaces(request):
    deskspaces = Deskspace.objects.all()
    labspaces = Labspace.objects.all()

    spaces = list(deskspaces) + list(labspaces)

    return render(request, 'space/space.html', {'spaces': spaces})
