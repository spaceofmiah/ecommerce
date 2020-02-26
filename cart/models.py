from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


### retrieve the configured underlying product from settings 
### or use the default product instead
UNDERLYING_PRODUCT_MODEL = getattr(
                                    settings, 
                                    'UNDERLYING_PRODUCT_MODEL', 
                                    "DefaultProduct")



class DefaultProduct (models.Model):
    '''
    A minimal product model
    '''
    name = models.CharField(max_length=100, blank=False)
    brand = models.CharField(max_length=100, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    available_in_stock = models.IntegerField(default=1)
    review = models.IntegerField(default=0)

    def __str__(self):
        return self.name.title()
        


class CartItem(models.Model):
    '''
    A model that represents item that can be
    added to cart
    '''
    date_added = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(
        UNDERLYING_PRODUCT_MODEL,
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

    def get_underlying_image(self):
        """
        returns image of the underlying product that
        forms a cart item
        """
        return self.product.image.url

    def get_absolute_url(self):
        """
        returns the actual url of the cart item
        """
        return self.product.get_absolut_url()

    def augment_quantity(self):
        """
        Increase the quantity of an existing cart item by 1
        if the item is to be added again
        """
        self.quantity = self.quantity + 1
        self.save()

    def total_price(self):
        """
        calculates the total price of a cart item
        :: cart_item_price * quantity_eadded_to_cart
        """
        return self.product.price * self.quantity





class Cart(models.Model):
    '''
    Cart 
    '''
    date_created = models.DateTimeField(
        auto_now_add=True
    )

    ticket = models.CharField(
        max_length=100, 
        editable=False
    )

    # this is true if checkout has not been called on 
    # the items within a cart, it becomes false if otherwise
    pending = models.BooleanField(default=True)

    # user = models.ForeignKey(
    #     User, 
    #     on_delete=models.CASCADE, 
    #     related_name='carts'
    # )

    items = models.ManyToManyField(
        CartItem, 
        related_name='belongs_to'
    )

    class Meta:
        verbose_name_plural = 'Cart'
        verbose_name = 'Cart'

    ### ** Helper Methods ** ##

    def __str__(self):
        """
        Returns string representation of object
        """
        return self.ticket

    def get_total_item(self):
        """
        Returns the total number of items present
        within cart
        """
        total_item_count = 0
        for item in self.items.all():
            total_item_count += item.quantity
        return total_item_count

    def get_total_amount(self):
        """
        Returns the total number of items present
        within cart
        """
        total_item_price = 0
        for item in self.items.all():
            total_item_price += (item.product.price * item.quantity)
        return total_item_price
    

    # An online cart cannot have two distinct representation of 
    # a cart item within a cart unlike our basket when we go to  
    # grocery stores that we can have two different oranges in 
    # same shopping basket.
    # So whenever a cart item that already exists in our cart
    # is to be readded, we'll just increment quantity property 
    # of the existing cart item
