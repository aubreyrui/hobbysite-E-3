from django.urls import path
from .views import (
    ProductDetailView, ProductListView, ProductCartList, ProductCreateView, ProductTransactionList, ProductUpdateView
)

urlpatterns = [
    path('items', ProductListView.as_view(), name="product_list"),
    path('item/<int:pk>', ProductDetailView.as_view(), name="product_detail"),
]

app_name = "merchstore"

'''
Product List View: /merchstore/items
Product Detail View: /merchstore/item/1
Product Create View : /merchstore/item/add
Product Update View: /merchstore/item/1/edit
Cart View: /merchstore/cart
Transactions List View: /merchstore/transactions

'''