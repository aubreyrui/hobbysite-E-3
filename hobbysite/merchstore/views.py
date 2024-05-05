from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product, Transaction
from .forms import CreateProductForm, TransactionForm

class ProductListView(ListView):
    model = Product
    template_name = 'merch_product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'merch_product_detail.html'
    form_class = TransactionForm

class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    tempalte_name = 'merch_create.html'
    form_class = CreateProductForm

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    tempalte_name = 'merch_update.html'
    form_class = CreateProductForm

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        form.instance.product = Product.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy(
            "merchstore:product_detail", kwargs={"pk":self.object.product.pk}
        )

class ProductCartList(ListView, LoginRequiredMixin):
    model = Transaction
    template_name = 'merch_cart.html'

class ProductTransactionList(ListView, LoginRequiredMixin):
    model = Transaction
    template_name = 'merch_transaction.html'

# Create your views here.
