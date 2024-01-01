from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('store'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NpAo2KCfqKcX0XkIFMz60a5WJKP6C468ClwGlh2187FvYFAGQYPPNkdlKunERmCKB2zfry2ibMC220nUDVtzJVY00ZOEpkXwK',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
