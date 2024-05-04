from django.urls import path
from .views import (
    ProductDetailView, ProductListView, ProductCartList, ProductCreateView, ProductTransactionList, ProductUpdateView
)

urlpatterns = [
<<<<<<< HEAD
    path('/items', ProductListView.as_view(), name="product_list"),
    path('/item/<int:pk>', ProductDetailView.as_view(), name="product_detail"),
    path('/item/add', ProductCreateView.as_view(), name="product_create"),
    path('/item/<int:pk>.edit',ProductUpdateView.as_view(), name="product_update"),
    path('/transactions', ProductTransactionList.as_view(), name="product_transaction"),
    path('/cart', ProductCartList.as_view(), name ="product_cart")
=======
    path('items', ProductListView.as_view(), name="product_list"),
    path('item/<int:pk>', ProductDetailView.as_view(), name="product_detail"),
>>>>>>> 94c71c04d2f3762380d36f8551728a3504fe181e
]

app_name = "merchstore"

"""
Product List View: /merchstore/items
Product Detail View: /merchstore/item/1
Product Create View : /merchstore/item/add
Product Update View: /merchstore/item/1/edit
Cart View: /merchstore/cart
Transactions List View: /merchstore/transactions

"""