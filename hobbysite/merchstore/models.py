from django.db import models
from django.urls import reverse
from user_management.models import Profile
from django.core.validators import MinValueValidator, MaxValueValidator

class ProductType(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class meta:
            ordering = ['name']

def stockstate():
    if Product.stock == 0:
        return "Out of Stock"
    else:
        return "Available"

class Product(models.Model):
    SALE = "SALE"
    AVAIL = "AVAIL"
    statuschoice = {
        SALE: "On Sale",
        AVAIL: "Available"
    }
    name = models.CharField(max_length = 255)
    description = models.TextField()
    producttype = models.ForeignKey(ProductType, null=True, on_delete=models.SET_NULL, related_name = 'products')
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    owner = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0,
        validators=[
            MinValueValidator(0, "Number of stock should be nonnegative!")
        ]
    )
    status = models.CharField(max_length=255, default=stockstate, choices=statuschoice)

    @property
    def __str__(self):
        return self.name
    
    def getStock(self):
        return self.stock

    def get_absolute_url(self):
        return reverse('merchstore:product_detail', args=str(self.pk))

    class meta:
        ordering = ['name']

class Transaction(models.Model):
    CART = "CRT"
    PAY = "PAY"
    SHIP = "SHIP"
    RECEIVE = "RECEIVE"
    DELIVER = "DELIVER"

    TransactionChoices = {
        CART: "On Cart",
        PAY: "To Pay",
        SHIP: "To Ship",
        RECEIVE: "To Receive",
        DELIVER: "Delivered"
    }
    buyer = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL) #add the profile (will determine this soon)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField(
        validators=[   
            MinValueValidator(1, "Amount should not be empty!") # to make sure that the buyer does not send the empty transaction form
        ]
    )
    status = models.CharField(max_length=255, choices=TransactionChoices)
    created_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('merchstore:transaction_detail', args=str(self.pk))
    
    def stock_validation(self):
        if (self.product.stock - self.amount) < 0:
            return "You can't purchase more than " + self.product.name + " available stock!"
        else:
            return "You can purchase!"
    
    def total(self):
        return self.amount*self.product.price
