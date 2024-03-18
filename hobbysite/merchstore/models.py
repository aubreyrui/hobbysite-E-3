from django.db import models

class ProductType(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    productype = models.ForeignKey('Product Type', on_delete=models.SET_NULL, related_name = 'products')
    price = models.IntegerField()
    
# Create your models here.
