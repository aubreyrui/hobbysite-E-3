from django.db import models
from django.urls import reverse

class ProductType(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('merchstore:product_list', args=str(self.pk))

class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    productype = models.ForeignKey('Product Type', on_delete=models.SET_NULL, related_name = 'products')
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absoute_url(self):
        return reverse('merchstore:product_detail', args=str(self.pk))
    
# Create your models here.
