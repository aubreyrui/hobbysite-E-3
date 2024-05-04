from django.db import models
from django.urls import reverse

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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('merchstore:product_detail', args=str(self.pk))

    class meta:
        ordering = ['name']

class Transaction(models.Model):
    buyer = models.ForeignKey(on_delete=models.SET_NULL) #add the profile (will determine this soon)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    amount = models.IntegerField()
    status = models.CharField()
    created_on = models.DateTimeField(auto_now_add=True)
    
# Create your models here.
