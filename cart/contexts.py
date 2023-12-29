from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from store.models import StoreItem


def cart_contents(request):

    cart_items = []
    total = 0
    storeitem_count = 0
    cart = request.session.get('cart', {})
    print(cart)

    for item_id, quantity in cart.items():
        storeitem = get_object_or_404(StoreItem, pk=item_id)
        print(storeitem)
        total += quantity * storeitem.price
        storeitem_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'storeitem': storeitem,
        })

    delivery = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'storeitem_count': storeitem_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
