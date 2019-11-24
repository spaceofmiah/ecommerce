from django.db import models
from clothing.models import Cloth


# Create your models here.
class CartItem(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(
        Cloth,
        related_name="+",
        on_delete = models.CASCADE
    )

    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name + "cart item"

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


