from django.contrib import admin
from cart.models import CartItem, Cart

admin.site.register(CartItem)
admin.site.register(Cart)