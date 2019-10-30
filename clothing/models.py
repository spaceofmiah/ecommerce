from django.db import models

# Create your models here.
class Cloth(models.Model):
    name = models.CharField(max_length=100)     
    size = models.CharField(max_length=3)       
    price = models.DecimalField(max_digits=999999, decimal_places=2)    
    material_type = models.CharField(max_length=100)        
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='clothes/images/')
    colour = models.CharField(max_length=30, default="black")
    amount = models.IntegerField()

    def __str__(self):
        return self.name.title()

      

    