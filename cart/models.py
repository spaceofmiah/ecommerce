from django.db import models
from django.conf import settings



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



# Create your models here.
class CartItem(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(
        UNDERLYING_PRODUCT_MODEL,
        related_name="+",
        on_delete = models.CASCADE
    )

    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name + "cart item"

    def augment_quantity(self):
        """
        Increase the quantity of an existing cart item by 1
        if the item is to be added again
        """
        self.quantity = self.quantity + 1
        self.save()

    def get_underlying_image(self):
        """
        returns image of the underlying product that
        forms a cart item
        """
        return self.product.image.url

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


    items = models.ManyToManyField(
        CartItem, 
        related_name='+'
    )

    def __str__(self):
        return self.ticket

