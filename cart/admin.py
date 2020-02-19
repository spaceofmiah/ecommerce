from django.contrib import admin
from cart.models import Cart, CartItem


# Register your models here.

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'date_added']

class CartAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'get_total_amount']

admin.site.register(CartItem, CartItemAdmin)
admin.site.register (Cart, CartAdmin)
