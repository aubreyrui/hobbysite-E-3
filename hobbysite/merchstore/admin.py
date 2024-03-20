from django.contrib import admin
from .models import Product, ProductType

# Register your models here.

class ProductInLine(admin.TabularInline):
    model = Product

class ProductTypeInLine(admin.TabularInline):
    model = ProductType

class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    inlines = [ProductInLine,]

    list_display = ['name',]
    ordering = ['-name',]

class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = ['name', 'price',]
    search_fields = ['name',]
    ordering = ['-name',]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)


# Register your models here.
# added comments to make this file visible (for a weird reason)
