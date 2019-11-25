import uuid

from cart.models import Cart



def _create_cart():
    cart = Cart(ticket = str(uuid.uuid4()))
    cart.save()
    return cart
