from django.urls import path
from cart import views


app_name = "cart"
urlpatterns = [
    path(
            '', 
            views.cart_list, 
            name='cart_list'
    ),

    path(
            'add-to-cart/<int:product_id>', 
            views.add_product_to_cart, 
            name='add_to_cart'
    ),

    path(
            'remove-from-cart/<int:item_id>',
            views.remove_item_from_cart,
            name="remove_from_cart"
    ),

    path(
            'complete-checkout',
            views.process_complete_checkout,
            name="complete_checkout"
    ),

    path(
            'increase-quantity',
            views.increment_quantity,
            name='increment_quantity'
    ),

    path(
            'payment-success',
            views.success_view,
            name='payment_success'
    ),
]