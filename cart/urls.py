from django.urls import path
from cart import views


app_name = "cart"
urlpatterns = [
    path(
            'add-to-cart/<int:product_id>', 
            views.add_product_to_cart, 
            name='add_to_cart'
    ),

    path(
            '', 
            views.cart_list, 
            name='cart_list'
    ),

    path(
            'remove-from-cart/<int:item_id>',
            views.remove_item_from_cart,
            name="remove_from_cart"
    ),
]