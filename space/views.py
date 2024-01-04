from django.shortcuts import render
from .models import Space, Labspace, Deskspace


def spaces(request):
    spaces = Space.objects.all()
    deskspaces = Deskspace.objects.all()
    labspaces = Labspace.objects.all()

    return render(request, 'space/space.html', {
        'spaces': spaces,
        'deskspaces': deskspaces,
        'labspaces': labspaces, }
    )
