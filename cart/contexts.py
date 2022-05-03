from decimal import Decimal
from django.conf import settings

def cart_contents(request):

    cart_items = []
    product_count = 0
    total = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        free_delivery_difference = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_difference = 0
    
    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'product_count': product_count,
        'total': total,
        'delivery': delivery,
        'free_delivery_difference': free_delivery_difference,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    
    return context