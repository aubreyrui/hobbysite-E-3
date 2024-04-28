from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator

class ProductType(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class meta:
            ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    producttype = models.ForeignKey(ProductType, null=True, on_delete=models.SET_NULL, related_name = 'products')
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    stock = models.IntegerField(
         validators = [
            MinLengthValidator(0, "Stock value must be positive!")
        ]
    )
    status = models.CharField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('merchstore:product_detail', args=str(self.pk))
    
    def getStatus(self):
         if self.stock > 0:
              return "On Sale"
         else:
              return "Out of Stock"
         
    class meta:
        ordering = ['name']
""" 
Stock - whole number
Status - character field with the following options:
Available (This should be the default value)
On sale
Out of stock (when stock is 0)

 """
    
# Create your models here.
