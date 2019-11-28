"""
This middleware will be used to check if there is a 
cart present for the current user or not, and if not
a cart is assigned for the current user session

Middleware is same as what is called filter in jsp
that serves as a middle man between request and 
response flow.
"""
from django.utils import timezone
from django.contrib.sessions.models import Session


from cart.models import Cart
from cart.helpers import _create_cart




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
            pass
        else:
            """
                we never want to have more than one carts in the database
                it is also used to invalidate carts and delete 
                cart items. Say for instance the current cart is 
                not checkouted and, another get created, then we 
                don't want the items of the prior cart to exits
            """
            if Cart.objects.count() > 1:
                """
                    CHECK !!! CHECK !!! CHECK !!! CHECK !!! CHECK !!!
                    
                    If this check is not done, then we'll have so many 
                    cart within our database that are useless and 
                    worthless to us. 
                    There is no use for a cart that was not checkout (payment
                    wasn't processed)
                """
                ## iterate through the cart table
                for cart in Cart.objects.all():
                    ## delete all cart item within each cart instances 
                    ## and then delete the cart itself if it's pending
                    ## property is true
                    if cart.pending:
                        ## delete the items within the cart only when 
                        ## it have more one or more cart item within 
                        ## itself
                        if cart.items.count() > 0:
                            [ item.delete() for item in cart.items.all() ]

                        ## delete the cart itself
                        cart.delete()
                    
                    """
                        CHECK !!! CHECK !!! CHECK !!! CHECK !!! CHECK !!!
                        
                        Not that if the above does not execute it means that
                        during the checkout (processing of cart payement),
                        the attribute of the cart in concern was set to False
                        ( this will be done in the view handling request for 
                        checkout )

                        cart.pending = False
                        cart.save()
                    """
                        
                        

            # if no cart is present for the user, then create a
            # create one
            cart  = _create_cart()
            request.session['cart'] = cart.id
            request.session['cart_present'] = True

            # the above set cart properties in session will
            # be deleted when a checkout process is done

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response