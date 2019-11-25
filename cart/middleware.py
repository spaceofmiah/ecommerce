"""
This middleware will be used to check if there is a 
cart present for the current user or not, and if not
a cart is assigned for the current user session
Middleware is same as what is called filter in jsp
that serves as a middle man between request and 
response flow.
"""

from cart.helpers import _create_cart




class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.session.get('cart_present', False):
            # if a cart is present for the user, 
            # then there is no need to do anything
            print("*** cart is present ***")
            pass
        else:
            # if no cart is present for the user, then
            # create one
            cart  = _create_cart()
            request.session['cart'] = cart.id
            request.session['cart_present'] = True

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response 