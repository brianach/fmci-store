from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Store

# Create your views here.

def store(request):
    """ A view to return store page """

    store = Store.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('store'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            store = store.filter(queries)

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