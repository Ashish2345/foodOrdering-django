from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            carts = Cart.objects.filter(cart_id=_cart_id(request))

            cart_items = CartItem.objects.all().filter(cart=carts[:1])

            for cart_items in cart_items:
                count = count + cart_items.quantity
        except Cart.DoesNotExist:
            count = 0
    return dict(count=count)
