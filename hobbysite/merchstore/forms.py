from django import forms

from .models import Product, Transaction

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['author']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'