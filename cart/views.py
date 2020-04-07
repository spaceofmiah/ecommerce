import math
from django.apps import apps
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render, 
    reverse, 
    redirect,
    get_object_or_404, 
)
from cart.models import (
    DefaultProduct, 
    Cart, 
    UNDERLYING_PRODUCT_MODEL,
    CartItem,
)
from cart.utils import (
    add_to_cart, 
    remove_from_cart, 
    get_cart_items, 
    get_total_item_price
)

import stripe


# https://docs.djangoproject.com/en/2.2/topics/settings/#calling-django-setup-is-required-for-standalone-django-usage
# helpful link
### if an underlying product model is configured, get the real 
### model
if type(UNDERLYING_PRODUCT_MODEL) == str:
    path = UNDERLYING_PRODUCT_MODEL.split('.')
    UNDERLYING_PRODUCT_MODEL = apps.get_model(path[0], path[1])


## Setup stripe secret key
stripe.api_key = settings.STRIPE_SECRET_KEY


def cart_list(request):
    '''
    returns a list of all available carts, 
    both pending and completed. 
    A cart is pending when a checkout has not been done
    A cart is completed when checkout has been done.
    '''
    cart_items = get_cart_items(request)
    items_total_amount = get_total_item_price(request)
    return render(request, 'cart/cart_list.html', {
        'cart': cart_items,
        'items_total_amount': items_total_amount,
    })


def add_product_to_cart(request, product_id):
    '''
    handles request to add a product to cart
    '''
    # retrieve the product that's to be added to cart
    product = get_object_or_404(
        UNDERLYING_PRODUCT_MODEL, pk=product_id)
    
    # add the product to cart
    cart = add_to_cart(request, product)
    return HttpResponseRedirect(reverse('clothing:index'))



def remove_item_from_cart(request, item_id):
    """
    handles request to remove a cart item from cart
    : request -- HttpRequest object
    : item_id -- Integer serving as a Cart Item unique identity
    """
    cart_item = get_object_or_404(CartItem, pk=item_id)
    remove_from_cart(request, cart_item)
    return redirect('cart:cart_list')



@login_required
def process_complete_checkout(request):
    cart_items = []
    # get the user's cart from session
    if (request.session['cart_present']):
        cart_id = request.session['cart']    
        cart = Cart.objects.get(pk=cart_id)
        cart_items = cart.items.all()


        # place all items in a user's cart (which are the items to be checkout) in a
        # list of dictionary where each dictionary represents an item in a user's
        # cart. below code shows a sample of how to iterate on cart object
        list_of_items = list()
        for item in cart_items:
            item = {
                'name': item.product.name,
                'description': item.product.description,
                'images': [item.get_underlying_image(),],
                'amount': math.ceil(item.total_price()*100),
                'currency': 'EUR',
                'quantity': item.quantity
            }
            list_of_items.append(item)
        
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items = list_of_items,
            # when user completes payment successfully, they'll be redirected to here
            success_url='http://localhost:8000/cart/payment-success?session_id={CHECKOUT_SESSION_ID}',
            # when user decide on checkout page that they don't want to proceed with payment
            # then they'll be redirected here
            cancel_url='http://localhost:8000/',
        )

    context = {'CHECKOUT_SESSION_ID': session.id, 'cart_items': cart_items,}
    return render(request, "cart/complete_checkout.html", context)



def increment_quantity(request):
    quantity = int(request.POST.get('quantity'))
    item_id = int(request.POST.get('item_id'))
    item = get_object_or_404(CartItem, id=item_id)

    if quantity < 1:
        quantity = 1
    item.quantity = quantity
    item.save()

    cart_items = get_cart_items(request)
    request.session.modified = True
    return redirect('cart:cart_list')



def success_view(request):
    return render(request, 'cart/success.html')