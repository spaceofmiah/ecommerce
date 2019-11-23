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

    def ___str___(self):
        return self.product.name + "cloth item"

