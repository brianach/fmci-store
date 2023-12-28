from decimal import Decimal
from django.conf import settings

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0

    delivery = 0
    
    grand_total = delivery + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'store_count': store_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context