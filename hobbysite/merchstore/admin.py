from django.contrib import admin
from .models import Product, ProductType, Transaction

# Register your models here.

class ProductInLine(admin.TabularInline):
    model = Product

class ProductTypeInLine(admin.TabularInline):
    model = ProductType

class TransactionInLine(admin.TabularInline):
    model = Transaction

class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    inlines = [ProductInLine,]

    list_display = ['name',]
    ordering = ['name',]

class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = ['owner','name', 'price','stock',]
    search_fields = ['name',]
    ordering = ['owner','name',]

class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ['buyer',]
    ordering = ['buyer',]



admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Transaction, TransactionAdmin)


# Register your models here.