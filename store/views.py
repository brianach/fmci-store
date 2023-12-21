from django.shortcuts import render
from .models import Store

# Create your views here.

def store(request):
    """ A view to return store page """

    store = Store.objects.all()

    context = {
        'store': store,
    }

    return render(request, 'store/store.html', context)