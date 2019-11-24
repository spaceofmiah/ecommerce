from django.contrib import admin
from django.conf import settings
from cart.models import CartItem, Cart, DefaultProduct

DISPLAY_DEFAULT_CART_PRODUCT = getattr(settings, 'DISPLAY_DEFAULT_CART_PRODUCT', False)

if DISPLAY_DEFAULT_CART_PRODUCT:
    admin.site.register(DefaultProduct)
    
admin.site.register(CartItem)
admin.site.register(Cart)