import uuid

from django.shortcuts import render, get_object_or_404
from cart.models import CartItem, Cart



def _create_cart():
    cart = Cart(ticket = str(uuid.uuid4()))
    cart.save()
    return cart


def add_to_cart(request, product):
    """
    adds an item with the above id to cart and increments
    the quantity of the item when it's already present in 
    cart

    : request -- an HTTP request object
    : product -- the product to be added to cart
    """
    # - get the cart id of the requesting user from session
    # an if non is found create one for the user

    # - retrieve the cart from the Cart object

    # - check if the item whose id is passed is already present 
    # within the retrieved cart of the requesting user
    
    # - if present, increase the quantity by one
          
    # - create new cart item and include to cart
    pass




## ** Helper Methods Definition ** #

def _create_cart_item_helper(product):
    """
    creates and return a new cart item

    : product -- this is the product that is to be
    added to cart
    """
    return CartItem.objects.create(product = product)

