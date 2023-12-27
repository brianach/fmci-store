from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Store, Category

# Create your views here.

def store(request):
    """ A view to return store page """

    store = Store.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                store = store.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            store = store.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            store = store.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('store'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            store = store.filter(queries)

    current_sorting = f'{sort}_{direction}'

    current_category = request.GET.get('category', 'Store')

    context = {
        'store': store,
        'search_term': query,
        'current_categories': categories,
        #'current_sorting': current_sorting,
        'current_category': current_category,
    }

    return render(request, 'store.html', context)

    
def store_detail(request, store_id):
    """ A view to show individual store details """

    storeitem = get_object_or_404(Store, pk=store_id)
    context = {
        'storeitem': storeitem,
    }

    return render(request, 'store_detail.html', context)