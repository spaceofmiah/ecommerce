from django.db import models
from django.contrib.auth.models import User

from clothing.models import Cloth

class CartItem(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(
        Cloth,
        related_name="+",
        on_delete = models.CASCADE
    )

    quantity = models.IntegerField(default=1)


    class Meta:
        verbose_name_plural = 'Cart Item'
        verbose_name = 'Cart Item'

    ### Helper Methods ###

    def __str__(self):
        """
        returns string representation of objects
        """
        return self.product.name

    def get_underlying_id(self):
        """
        returns id of the underlying product that forms
        a cart item
        """
        return self.product.id

    def get_absolute_url(self):
        """
        returns the actual url of the cart item
        """
        return self.product.get_absolute_url()

    def augment_quantity(self, quantity):
        """
        Increase the quantity of an existing cart item by 1
        if the item is to be added again
        """
        self.quantity = self.quantity + int(quantity)
        self.save()

    def total_price(self):
        """
        calculates the total price of a cart item
        :: cart_item_price * quantity_added_to_cart
        """
        return self.product.price * self.quantity





class Cart(models.Model):
    ticket = models.CharField(max_length=100, editable=False)
    items = models.ManyToManyField("CartItem", related_name='+')

    class Meta:
        verbose_name_plural = 'Cart'
        verbose_name = 'Cart'

    ### ** Helper Methods ** ##

    def __str__(self):
        """
        Returns string representation of object
        """
        return self.ticket
    

    # An online cart cannot have two distinct representation of 
    # a cart item within a cart unlike our basket when we go to  
    # grocery stores that we can have two different oranges in 
    # same shopping basket.
    # So whenever a cart item that already exists in our cart
    # is to be readded, we'll just increment quantity property 
    # of the existing cart item
    
        