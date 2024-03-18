from django.urls import path
from .views import ProductTypeView, ProductDetailView

urlpatterns = [
    path('merchstore/items', ProductTypeView.as_view(), name="products"),
    path('merchstore/item/<int:pk>', ProductDetailView.as_view(), name="product_detail"),
]

app_name = "merchstore"