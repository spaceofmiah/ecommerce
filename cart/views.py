from django.shortcuts import render
from django.apps import apps
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from cart.models import DefaultProduct, Cart, UNDERLYING_PRODUCT_MODEL
from cart.helpers import add_to_cart

# Create your views here.


### if an underlying product model is configured in settings, get the real 
### model as what was
if type(UNDERLYING_PRODUCT_MODEL) == str:
    path = UNDERLYING_PRODUCT_MODEL.split('.')
    UNDERLYING_PRODUCT_MODEL = apps.get_model(path[0], path[1])



def add_product_to_cart(request, product_id):
    '''
    handles request to add a product to cart

    : request : HttpRequest object
    : product_id : the unique identity of the UNDERLYING_PRODUCT_MODEL
    '''
    # retrieve the product that's to be added to cart
    product = get_object_or_404(
        UNDERLYING_PRODUCT_MODEL, pk=product_id)
    
    # add the product to cart by using add_to_cart helper method
    cart = add_to_cart(request, product)
    return HttpResponseRedirect(reverse('clothing:index'))


def cart_list(request):
    '''
    Retrieves all cart items saved in a variable within the cart
     and return a response to the user 
     '''
    cart_items = []
    # get the user's cart from session
    if (request.session['cart_present']):
        cart_id = request.session['cart']    
        cart = Cart.objects.get(pk=cart_id)
        cart_items = cart.items.all()
    

    return render(request, 'cart/cart_list.html', {
        'cart': cart_items
    })