from django.contrib import admin
from .models import Product, ProductType

# Register your models here.

class ProductInLine(admin.TabularInline):
    model = Product

class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    inlines = [ProductInLine,]

class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = ['name', 'price',]
    search_fields = ['name',]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)


# Register your models here.
