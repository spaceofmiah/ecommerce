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


def _create_cart_item_helper(product):
    """
    : private access
    creates and return a new cart item
    : product -- this is the product that is to be
    added to cart
    """
    cart_item = CartItem.objects.create(product = product)
    return cart_item



def add_to_cart(request, product):
    """
    adds a product to cart and increments
    the quantity of the item when it's already present in 
    cart
    : request -- an HTTP request object
    : product -- the product to be added to cart
    """
    # - get the cart id of the requesting user from session
    if request.session.get('cart', False):
        pass
    else:
        # if no cart is present for the user, then create a
        # create one
        cart  = _create_cart()
        request.session['cart'] = cart.id
        request.session['cart_present'] = True
        request.session['cart_item_count'] = cart.get_total_item()


    cart_id = int(request.session['cart'])

    # - retrieve the cart from the Cart object
    cart = get_object_or_404(Cart, pk=cart_id)

    # - check if passed product  is already present  within the 
    # CartItem table


    # check if the product to be added matches any of CartItem's
    # underlying product id 
    if CartItem.objects.filter(product__id=product.id).exists():
        # if there is a match, retrieve the CartItem that matches
        # the above check
        cart_item = CartItem.objects.get(product__id=product.id)

        # since we can have various cart object in our database
        # we need to confirm if the cart_item whose underlying 
        # product exists belongs to the current cart object

        # if the current cart is not amongst other cart object
        # that the cart_item belongs to, then add it.
        if cart not in cart_item.belongs_to.all() and cart.pending:
            """
                CHECK !!! CHECK !!! CHECK !!! CHECK !!! CHECK !!!
                
                If this check is not done, then we'll have a cart
                that is not retaining an added cart item  solely 
                because the item is already present in another cart 
                that is not in use by the current current session
            """
            cart_item.quantity = 1
            cart_item.save()
            cart.items.add(cart_item)
        else:
            # if the current cart is amongst the the other carts
            # that the cart_item belongs to, then increase it's 
            # quanity
            cart_item.augment_quantity()
    else:
        # create and add cartitem to cart if there is n
        cart_item = _create_cart_item_helper(product)
        cart.items.add(cart_item)
        cart.save()
    return cart




def remove_from_cart(request, cart_item):
    """
    helps to remove a cart item from the cart saved in the
    current request session object
    : request -- HttpRequest object
    : cart_item -- An instance of cart_item
    """
    # - get the cart id of the requesting user from session
    cart_id = int(request.session['cart'])

    # - retrieve the cart from the Cart object
    cart = get_object_or_404(Cart, pk=cart_id)

    # - remove the item from the cart
    cart.items.remove(cart_item)




def get_cart_items(request):
    # get the user's cart from session
    if (request.session['cart_present']):
        cart_id = request.session['cart']    
        cart = Cart.objects.get(pk=cart_id)
        return cart.items.all()
    return []