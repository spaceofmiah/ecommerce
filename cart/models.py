from django.db import models
from django.contrib.auth.models import User

from clothing.models import Cloth

class CartItem(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    # a ForeignKey is unique by default, making it the other
    # way round allows it to hold more than one object of 
    # same kind. An online cart cannot vitually hold two of 
    # same object unlike our basket when we go to grocery 
    # store, and that is why if a product of same kind that
    # already exists in our cart is to be readded, we'll just
    # increment the quantity property of the existing product
    # hence our quantity field below
    product = models.ForeignKey(
        Cloth,
        related_name="+",
        on_delete = models.CASCADE,
        unique=False        # this here does the trick
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

    def get_absolute_url(self):
        """
        returns the actual url of the cart item
        """
        return self.product.get_absolute_url()

    def augment_quantity(self):
        """
        Increase the quantity of an existing cart item by 1
        if the item is to be added again
        """
        self.quantity += 1
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