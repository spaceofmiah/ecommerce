from django.db import models

class Cloth(models.Model):
    """
    a model for cloth object
    """
    name = models.CharField(max_length=100)     
    size = models.CharField(max_length=3)       
    price = models.DecimalField(max_digits=999999, decimal_places=2)    
    material_type = models.CharField(max_length=100)        
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='clothes/images/')
    available_in_stock = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        """
        String representation of object
        """
        return self.name.title()