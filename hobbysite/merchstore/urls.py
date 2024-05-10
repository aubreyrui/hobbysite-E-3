from django.urls import path
from .views import (
    ProductDetailView, ProductListView, ProductCartList, ProductCreateView, ProductTransactionList, ProductUpdateView
)

urlpatterns = [
    path('items', ProductListView.as_view(), name="product_list"),
    path('item/<int:pk>', ProductDetailView.as_view(), name="product_detail"),
    path('item/add', ProductCreateView.as_view(), name="product_create"),
    path('item/<int:pk>/edit',ProductUpdateView.as_view(), name="product_update"),
    path('transactions', ProductTransactionList.as_view(), name="product_transaction"),
    path('cart', ProductCartList.as_view(), name ="product_cart")
]

app_name = "merchstore"