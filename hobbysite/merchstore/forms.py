from django import forms

from .models import Product, Transaction

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['owner']

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['owner']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount']