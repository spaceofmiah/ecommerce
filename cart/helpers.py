import uuid

from django.shortcuts import render, get_object_or_404
from cart.models import CartItem, Cart



def _create_cart():
    """
    : private access
    create and returns a cart object
    """
    cart = Cart(ticket = str(uuid.uuid4()))
    cart.save()
    return cart


def add_to_cart(request, product):
    """
    adds a product to cart and increments
    the quantity of the item when it's already present in 
    cart

    : request -- an HTTP request object
    : product -- the product to be added to cart
    """
    # - get the cart id of the requesting user from session
    cart_id = int(request.session['cart'])

    # - retrieve the cart from the Cart object
    cart = get_object_or_404(Cart, pk=cart_id)

    # - check if passed product  is already present  within the 
    # retrieved cart of the requesting user

   
    # check if the id of cart items underlying id and product
    # to be added id are same
    if CartItem.objects.filter(product__id=product.id).exists():
        cart_item = CartItem.objects.get(product__id=product.id)
        # if same, then increase the cart item quanity instead
        cart_item.augment_quantity()
    else:
        # add the product
        cart_item = _create_cart_item_helper(product)
        cart.items.add(cart_item)
    
    return cart




## ** Helper Methods Definition ** #

def _create_cart_item_helper(product):
    """
    : private access
    creates and return a new cart item

    : product -- this is the product that is to be
    added to cart
    """
    cart_item = CartItem.objects.create(product = product)
    print(f"{cart_item} created sucessfully")
    return cart_item

