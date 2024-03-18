from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product, ProductType

class ProductTypeView(ListView):
    model = ProductType
    template_name = 'product_type.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

# Create your views here.
