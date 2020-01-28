from django.contrib import admin
from cart.models import Cart, CartItem


# Register your models here.

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'date_added']

admin.site.register(CartItem, CartItemAdmin)
admin.site.register (Cart)
