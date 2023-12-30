from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from store.models import StoreItem


def cart_contents(request):

    cart_items = []
    total = 0
    subtotal = 0
    cart_total = 0
    storeitem_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        print(item_id, item_data,)
        if isinstance(item_data, int):
            storeitem = get_object_or_404(StoreItem, pk=item_id)
            quantity = item_data
            subtotal = quantity * storeitem.price
            cart_total += subtotal
            storeitem_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'storeitem': storeitem,
                'subtotal': subtotal,
            })

        else:
            storeitem = get_object_or_404(StoreItem, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                subtotal = quantity * storeitem.price
                cart_total += subtotal
                storeitem_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'storeitem': storeitem,
                    'size': size,
                    'subtotal': subtotal,
                })

    delivery = 0

    grand_total = delivery + cart_total

    context = {
        'cart_items': cart_items,
        'storeitem_count': storeitem_count,
        'cart_total': cart_total,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
