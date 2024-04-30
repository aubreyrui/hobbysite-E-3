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
            MinLengthValidator(0, "Stock value must be nonnegative!")
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

class Transaction(models.Model):
    buyer = models.ForeignKey(on_delete=models.SET_NULL) #add the profile (will determine this soon)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    amount = models.IntegerField()
    status = models.CharField()
    created_on = models.DateTimeField(auto_now_add=True)
""" 
Stock - whole number
Status - character field with the following options:
Available (This should be the default value)
On sale
Out of stock (when stock is 0)

Transaction
Buyer - foreign key to Profile, set to NULL when deleted
Product - foreign key to Product, set to NULL when deleted
Amount - whole number which is the amount of Product to buy
Status - character field with the following options:
On cart
To Pay
To Ship
To Receive
Delivered
Created On - datetime field, only gets set when the model is created


 """
    
# Create your models here.
