from django.shortcuts import render, get_object_or_404
from .models import Store

# Create your views here.

def store(request):
    """ A view to return store page """

    store = Store.objects.all()

    context = {
        'store': store,
    }

    return render(request, 'store.html', context)

    
def store_detail(request, store_id):
    """ A view to show individual store details """

    storeitem = get_object_or_404(Store, pk=store_id)
    context = {
        'storeitem': storeitem,
    }

    return render(request, 'store_detail.html', context)