from django.apps import apps
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from cart.models import DefaultProduct, Cart, UNDERLYING_PRODUCT_MODEL
from cart.helpers import add_to_cart


# https://docs.djangoproject.com/en/2.2/topics/settings/#calling-django-setup-is-required-for-standalone-django-usage
# helpful link
### if an underlying product model is configured, get the real 
### model
if type(UNDERLYING_PRODUCT_MODEL) == str:
    path = UNDERLYING_PRODUCT_MODEL.split('.')
    UNDERLYING_PRODUCT_MODEL = apps.get_model(path[0], path[1])


def cart_list(request):
    '''
    returns a list of all available carts, 
    both pending and completed. 

    A cart is pending when a checkout has not been done
    A cart is completed when checkout has been done.
    '''
    all_cart = Cart.objects.all()
    return render(request, 'cart/cart_list.html', {
        'carts': all_cart
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