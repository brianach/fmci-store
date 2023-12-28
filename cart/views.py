from django.shortcuts import render

# Create your views here.

def cart(request):
    """ A view that renders the bag contents page """

    return render(request, 'cart/cart.html')