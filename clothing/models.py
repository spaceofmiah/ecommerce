from django.db import models

# Create your models here.
class Cloth(models.Model):
    name = models.CharField(max_length=100)     # a cloth should have a name
    size = models.CharField(max_length=3)       # a cloth should have a size
    price = models.DecimalField(max_digits=999999, decimal_places=2)    # a cloth should have an
    # read more about DecimalField(https://docs.djangoproject.com/en/2.2/ref/models/fields/#decimalfield)
    material_type = models.CharField(max_length=100)        # a cloth should have a material_type
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='clothes/images/')
    