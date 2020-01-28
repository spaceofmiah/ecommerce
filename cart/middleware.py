from django.contrib.sessions.models import Session


from cart.models import Cart




class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        cart = ''

        if request.session.get('cart_present', False):
            # if a cart is present for the user, 
            # then retrieve the cart and get it's total item count
            cart = Cart.objects.get(pk=int(request.session['cart']))
            request.session['cart_item_count'] = cart.get_total_item()

        return self.get_response(request)
