from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product, Transaction

class ProductListView(ListView, LoginRequiredMixin):
    model = Product
    template_name = 'merch_product_list.html'

class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product
    template_name = 'merch_product_detail.html'

class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    tempalte_name = 'merch_create.html'

class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    tempalte_name = 'merch_update.html'

class ProductCartList(ListView, LoginRequiredMixin):
    model = Transaction
    template_name = 'merch_cart.html'


class ProductTransactionList(ListView, LoginRequiredMixin):
    model = Transaction
    template_name = 'merch_transaction.html'

# Create your views here.
