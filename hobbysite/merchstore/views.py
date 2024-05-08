from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login

from .models import Product, Transaction, ProductType
from user_management.models import Profile
from .forms import CreateProductForm, TransactionForm

class ProductListView(ListView):
    model = Product
    template_name = 'merch_product_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['product_types'] = ProductType.objects.all()
        return ctx

class ProductDetailView(DetailView):
    model = Product
    template_name = 'merch_product_detail.html'
    form_class = TransactionForm
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        form = TransactionForm()
        form.fields["amount"].widget.attrs['max'] = ctx['product'].stock # https://stackoverflow.com/questions/55287490/django-forms-min-and-max-price-inputs
        
        ctx["form"] = form
        return ctx
    
    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        product = self.get_object()
        if form.is_valid():
            if request.user.is_authenticated:
                transact = Transaction()
                transact.product = product
                transact.amount = form.cleaned_data["amount"]
                transact.buyer = request.user.profile
                transact.save() # posts the transaction
                product.stock -= form.cleaned_data["amount"]
                return redirect("merchstore:product_cart")
            else:
                return redirect_to_login(next=request.get_full_path())
            
        else:
            # repeating the process again
            self.object_list = self.get_queryset(**kwargs)
            ctx = self.get_context_data(**kwargs)
            ctx['form'] = form 
            return self.render_to_response(ctx)

class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    template_name = 'merch_create.html'
    form_class = CreateProductForm

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    template_name = 'merch_update.html'
    form_class = CreateProductForm

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        form.instance.product = Product.objects.get(pk=self.kwargs["pk"])
        if form.is_valid() and self.get_object().stock == 0:
            form.instance.status = "Out of Stock"
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
